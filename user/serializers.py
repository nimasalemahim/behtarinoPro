from rest_framework import serializers
from user.models import User, UserAddress


class GeneralUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name'
        )


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = (
            'id', 'title', 'lat', 'long'
        )


class UserAddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = (
            'user', 'title', 'lat', 'long'
        )


class AdminUserSerializer(serializers.ModelSerializer):
    count_addresses = serializers.IntegerField()
    addresses = UserAddressSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'count_addresses', 'addresses'
        )
