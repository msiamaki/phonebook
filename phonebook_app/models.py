from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name", blank=False)
    last_name = models.CharField(max_length=50, verbose_name="Last Name", blank=True)
    phone_number = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)],
        null=False,
        unique=True,
        verbose_name="Phone Number",
    )
    address = models.TextField(blank=True, verbose_name="Address")
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ("first_name", "last_name", "phone_number")

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
