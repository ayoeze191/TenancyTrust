from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('tenant', 'Tenant'),
        ('landlord', 'Landlord'),
    )

    phone_number = models.CharField(max_length=15, unique=True)
    nin = models.CharField(max_length=11, blank=True)
    bvn = models.CharField(max_length=11, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)