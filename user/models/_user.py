from django.db import models
from django.contrib.auth.models import AbstractUser
from ._modification import ModificationMixin


class User(AbstractUser, ModificationMixin):
    phone_number = models.CharField(max_length=50, null=True, blank=True)
# Create your models here.
