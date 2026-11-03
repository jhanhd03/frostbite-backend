from django.db import models
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='productos'
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)  # Peso -CLP
    formato = models.CharField(max_length=50)  # algo asi: "1 kg", "Bolsa 5 kg", "Cilindro"
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Validación del negocio: para evitar precios negativos
        if self.precio is not None and self.precio < 0:
            raise ValidationError({'precio': 'El precio no puede ser negativo.'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.formato})"


class Pedido(models.Model):
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        related_name='pedidos'
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Validación del negocio: no pedir 0 unidades
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': 'La cantidad debe ser mayor a 0.'})
        # Validación del negocio: verificar stock disponible
        if self.producto and self.cantidad > self.producto.stock:
            raise ValidationError({
                'cantidad': f'Stock insuficiente. Stock disponible: {self.producto.stock}'
            })

    def save(self, *args, **kwargs):
        self.clean()
        # calculo automatico de total y congelación del precio unitario
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        self.total = self.precio_unitario * self.cantidad
        
        # descontar stock del producto al confirmar pedido
        if self._state.adding:
            self.producto.stock -= self.cantidad
            self.producto.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido #{self.id} - {self.producto.nombre} x {self.cantidad}"