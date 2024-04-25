from django.db import models
from ERP_Project.models.manager2 import warehouse_product
from django.contrib.auth import get_user_model
User = get_user_model()


class filial(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class filial_product(models.Model):
    filial_id = models.ForeignKey(filial, on_delete=models.SET_NULL, null=True)
    warehouse_product_id = models.ForeignKey(warehouse_product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.filial_id

