from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, role, password=None, **extra_fields):
        if not role:
            raise ValueError('The role must be set')
        user = self.model(role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, role, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(role, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'admin'
    MANAGER1 = 'manager1'
    MANAGER2 = 'manager2'
    MANAGER3 = 'manager3'
    CASHIER = 'cashier'

    ROLES = [
        (ADMIN, 'admin'),
        (MANAGER1, 'manager1'),
        (MANAGER2, 'manager2'),
        (MANAGER3, 'manager3'),
        (CASHIER, 'cashier'),
    ]

    username = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=15, choices=ROLES, default=ADMIN)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.role
