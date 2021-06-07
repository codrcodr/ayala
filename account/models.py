from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.



class AccountManager(BaseUserManager):
    
    def create_user(self, email, username, password, full_name, **other_fields):
        if not email:
            raise ValueError("User must provide an email")

        if not password:
            raise ValueError("User must provide an password")

        normalized_email = self.normalize_email(email)
        user = self.model(
            email = normalized_email,
            username=username,
            full_name = full_name, 
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, full_name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_active') is not True:
            raise ValueError("Super user should be active")

        if other_fields.get('is_staff') is not True:
            raise ValueError("Super user staff should be enabled")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("Super user should be active")

        return self.create_user(email, username, password, full_name, **other_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=300)
    username = models.CharField(unique=True, max_length=255)
    full_name = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username']

    objects = AccountManager()

    def __str__(self):
        return self.full_name
