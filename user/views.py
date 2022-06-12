from .serializers import AdminUserSerializer, UserAddressCreateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import User
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserFilters


class GetUsersForAdminView(ListAPIView):
    serializer_class = AdminUserSerializer
    queryset = User.get_query_set_with_num_of_addresses_with_addresses(3)

    filter_backends = [DjangoFilterBackend, ]
    filter_class = UserFilters


class CreatAddressView(CreateAPIView):
    serializer_class = UserAddressCreateSerializer



