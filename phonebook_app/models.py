from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50, min_length=1, null=False)
    last_name = models.CharField(max_length=50, min_length=1, null=True)
    phone_number = models.CharField(max_length=11, min_length=11, null=False, unique=True)
    address = models.TextField(null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
