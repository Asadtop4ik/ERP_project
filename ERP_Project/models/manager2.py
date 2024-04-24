from ERP_Project.models.manager1 import brand
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class warehouse_product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    first_price = models.CharField(max_length=255)
    sale_price = models.CharField(max_length=255)
    brand = models.ForeignKey(brand, blank=True, null=True, on_delete=models.SET_NULL)
    reg_data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    where_to = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def is_in_count(self):
        return self.stock > 0

    def reduce_count(self, quantity):
        if self.stock < quantity:
            return False
        self.stock -= quantity
        self.save()
        return True

    def increase_stock(self, amount):
        self.stock += amount
        self.save()

    class Meta:
        ordering = ['name']
