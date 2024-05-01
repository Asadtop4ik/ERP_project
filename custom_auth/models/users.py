from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_("Email required field!"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    ADMIN = 'admin'
    MANAGER1 = 'manager1'
    MANAGER2 = 'manager2'
    MANAGER3 = 'manager3'
    CASHIER = 'cashier'

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MANAGER1, 'manager1'),
        (MANAGER2, 'manager2'),
        (MANAGER3, 'manager3'),
        (CASHIER, 'cashier'),
    )
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.password:
                self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
