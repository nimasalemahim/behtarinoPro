from django.contrib import admin
from user.models import User
from user.models import UserAddress


class UserAddressInLine(admin.TabularInline):
    model = UserAddress
    extra = 1


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'phone_number',)
    inlines = (UserAddressInLine,)
    search_fields = ('username',)


@admin.register(UserAddress)
class AdminUserAddress(admin.ModelAdmin):
    autocomplete_fields = ('user',)

# Register your models here.
