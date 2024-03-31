from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name="First Name")
    last_name = models.CharField(max_length=50, null=True, verbose_name="Last Name")
    phone_number = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)],
        null=False,
        unique=True,
        verbose_name="Phone Number",
    )
    address = models.TextField(null=True, verbose_name="Address")
    description = models.TextField(null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
