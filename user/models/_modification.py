from django.db import models
import datetime


class ModificationMixin(models.Model):
    uid = models.CharField(max_length=100, unique=True, null=True)
    _created_at = models.DateTimeField(auto_now_add=True, null=True)
    _updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at
