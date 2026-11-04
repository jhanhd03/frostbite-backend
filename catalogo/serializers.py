from rest_framework import serializers
from .models import Categoria, Producto, Pedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def validate_precio(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

    def validate(self, data):
        producto = data['producto']
        cantidad = data['cantidad']

        if cantidad <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor a 0.")

        if cantidad > producto.stock:
            raise serializers.ValidationError(
                f"Stock insuficiente. Stock actual: {producto.stock}"
            )

        return data