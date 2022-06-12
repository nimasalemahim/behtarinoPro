from django.db import models
from django.contrib.auth.models import AbstractUser
from ._modification import ModificationMixin
from django.db.models import Count


class User(AbstractUser, ModificationMixin):
    phone_number = models.CharField(max_length=50, null=True, blank=True)

    @staticmethod
    def get_query_set_with_num_of_addresses():
        return User.objects.annotate(count_addresses=Count('addresses'))
