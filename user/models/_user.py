from django.db import models
from django.contrib.auth.models import AbstractUser
from ._modification import ModificationMixin
from django.db.models import Count
from django.db.models import OuterRef, Subquery, Prefetch
from ._user_address import UserAddress


class User(AbstractUser, ModificationMixin):
    phone_number = models.CharField(max_length=50, null=True, blank=True)

    @staticmethod
    def get_query_set_with_num_of_addresses():
        return User.objects.annotate(count_addresses=Count('addresses'))

    @staticmethod
    def get_query_set_with_num_of_addresses_with_addresses(num_addresses=3):
        ids = Subquery(
            UserAddress.objects.filter(user_id=OuterRef('user_id')).values_list('id', flat=True)[:num_addresses])
        return User.objects.annotate(count_addresses=Count('addresses')).prefetch_related(
            Prefetch('addresses', queryset=UserAddress.objects.filter(id__in=ids)))
