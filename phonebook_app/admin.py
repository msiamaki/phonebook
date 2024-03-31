from django.contrib import admin
from django.contrib.admin import register 

from .models import Contact

# Register your models here.


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number")
    list_display_links = ("first_name",)
    search_fields = ("first_name", "last_name", "phone_number", "address")
