from django.contrib import admin
from django.contrib.admin import register 

from .models import Contact

# Register your models here.


@register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number", "date_created", "update_date")
    list_display_links = ("first_name",)
    list_editable = ("phone_number",)
    search_fields = ("first_name", "last_name", "phone_number", "address")
