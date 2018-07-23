from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', )

    class Meta:
        app_label = 'users'
        ordering = ('-email', )
        verbose_name = 'użytkownik'
        verbose_name_plural = 'użytkownicy'

    def __str__ (self):
        return '{} {}'.format(self.first_name, self.last_name)
