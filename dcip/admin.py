from django.contrib import admin
from .models import CidrAddress, MergedCidrAddress


@admin.register(CidrAddress)
class CidrAddressAdmin(admin.ModelAdmin):
    list_display = ["cidr", "provider"]
    list_filter = ["provider"]
    search_fields = ["cidr"]


@admin.register(MergedCidrAddress)
class MergedCidrAddressAdmin(admin.ModelAdmin):
    list_display = ["cidr", "provider"]
    list_filter = ["provider"]
    search_fields = ["cidr"]
