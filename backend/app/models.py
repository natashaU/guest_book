from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class GuestbookEntry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    comment = models.CharField(max_length=1023)
