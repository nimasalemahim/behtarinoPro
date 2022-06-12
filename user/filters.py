import django_filters
from .models import User


class UserFilters(django_filters.FilterSet):
    address_count_gt = django_filters.NumberFilter(method='filter_address_count_gt')
    address_count_lt = django_filters.NumberFilter(method='filter_address_count_lt')
    address_count_ex = django_filters.NumberFilter(method='filter_address_count_e')

    def filter_address_count_gt(self, queryset, name, value):
        return queryset.filter(count_addresses__gt=value)

    def filter_address_count_lt(self, queryset, name, value):
        return queryset.filter(count_addresses__lt=value)

    def filter_address_count_e(self, queryset, name, value):
        return queryset.filter(count_addresses=value)

    class Meta:
        model = User
        fields = ()
