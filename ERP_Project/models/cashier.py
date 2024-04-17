from django.db import models
from .manager2 import warehouse_product


pay_CHOICES = [
    ('cash', 'cash'),
    ('online_payment', 'online_payment'),
]


class customer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    product = models.ForeignKey(warehouse_product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    cash = models.CharField(choices=pay_CHOICES, max_length=255)

    def __str__(self):
        return f"{self.name} {self.phone_number}"


