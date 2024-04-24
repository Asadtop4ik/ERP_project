from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    first_price = models.CharField(max_length=255)
    sale_price = models.CharField(max_length=255)
    brand_id = models.ForeignKey(brand, blank=True, null=True, on_delete=models.SET_NULL)
    reg_data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    where_to = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name

