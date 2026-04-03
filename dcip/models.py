from django.db import models
from cidrfield.models import IPNetworkField

from .conf import get_provider_choices


class CidrAddress(models.Model):
    cidr = IPNetworkField(db_index=True, unique=True)
    provider = models.CharField(choices=get_provider_choices, max_length=2, db_index=True)

    def __str__(self):
        return "%s %s" % (self.get_provider_display(), self.cidr)


class MergedCidrAddress(models.Model):
    cidr = IPNetworkField(db_index=True, unique=True)
    provider = models.CharField(choices=get_provider_choices, max_length=2, db_index=True)

    def __str__(self):
        return "%s %s" % (self.get_provider_display(), self.cidr)
