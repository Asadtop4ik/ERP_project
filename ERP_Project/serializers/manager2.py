from rest_framework import serializers
from ERP_Project.models.manager2 import warehouse_product


class warehouse_productSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = warehouse_product
        fields = '__all__'





