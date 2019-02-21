from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=264, null=False, blank=False)
    address = models.TextField(max_length=500, null=False, blank=False)
    email = models.EmailField(max_length=70, null=False, blank=False)
    phone = models.CharField(max_length=14, null=False, blank=False)
    message = models.TextField(max_length=1000)

