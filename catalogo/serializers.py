from rest_framework import serializers
from .models import Categoria, Producto, Pedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']


class ProductoSerializer(serializers.ModelSerializer):
    
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')

    class Meta:
        model = Producto
        fields = [
            'id', 
            'nombre', 
            'categoria', 
            'categoria_nombre', 
            'precio', 
            'formato', 
            'descripcion', 
            'stock', 
            'disponible', 
            'fecha_creacion'
        ]

    def validate_precio(self, value):
        """Validación en el serializador para evitar precios negativos"""
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo.")
        return value

    def validate_stock(self, value):
        """Validación para evitar stock negativo"""
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value


class PedidoSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.ReadOnlyField(source='producto.nombre')

    class Meta:
        model = Pedido
        fields = [
            'id', 
            'producto', 
            'producto_nombre', 
            'cantidad', 
            'precio_unitario', 
            'total', 
            'fecha_pedido'
        ]
        read_only_fields = ['precio_unitario', 'total', 'fecha_pedido']

    def validate(self, data):
        """Validación de lógica de negocio para pedidos"""
        producto = data.get('producto')
        cantidad = data.get('cantidad', 1)

        if cantidad <= 0:
            raise serializers.ValidationError({"cantidad": "Debe solicitar al menos una unidad."})

        if producto and cantidad > producto.stock:
            raise serializers.ValidationError({
                "cantidad": f"Stock insuficiente para '{producto.nombre}'. Stock actual disponible: {producto.stock}"
            })

        return data