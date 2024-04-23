from django.contrib.auth.models import User
from rest_framework import serializers
from ERP_Project.models.manager1 import brand, product


class brandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = '__all__'


class productSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=brand.objects.all(), required=True)

    class Meta:
        model = product
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "is_staff", "is_active"]
        read_only_fields = [
            'id',
        ]
