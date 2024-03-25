from rest_framework import serializers
from ERP_Project.models.manager3 import filial, filial_product
from django.core.exceptions import ObjectDoesNotExist
from ERP_Project.models.manager2 import warehouse_product


class filialSerializer(serializers.ModelSerializer):
    class Meta:
        model = filial
        fields = '__all__'


class filial_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = filial_product
        fields = '__all__'

    def validate_quantity(self, value):
        try:
            # Fetch the product instance from the database
            product_id = self.initial_data['warehouse_product_id']
            product = warehouse_product.objects.get(id=product_id)

            # Check the stock
            if value > product.stock:
                raise serializers.ValidationError("Not enough items in stock.")

            if value < 1:
                raise serializers.ValidationError("Quantity must be at least 1.")

            return value

        except ObjectDoesNotExist:
            raise serializers.ValidationError("Product does not exist")

    def create(self, validated_data):
        count = filial_product.objects.create(**validated_data)
        product = count.warehouse_product_id
        product.stock -= count.quantity
        product.save()
        return count
