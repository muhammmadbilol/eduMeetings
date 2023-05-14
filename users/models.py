from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        # extra_fields['is_active'] = False
        user = self.validate(email, password, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        user = self.validate(email, password, **extra_fields)
        user.save(using=self._db)
        return user

    def validate(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
