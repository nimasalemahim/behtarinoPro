from django.db import models
from django.db.models import deletion
from ._modification import ModificationMixin


class UserAddress(ModificationMixin):
    user = models.ForeignKey('user.User', related_name='addresses', on_delete=deletion.CASCADE)
    title = models.TextField(blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    long = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    admin_created = models.BooleanField(default=False)

    class Meta:
        ordering = ['-_updated_at']

    @staticmethod
    def get_admin_created_users():
        return UserAddress.objects.filter(admin_created=True)


# Create your models here.
