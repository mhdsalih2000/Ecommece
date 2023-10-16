from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=15,blank=False)
    email = models.EmailField( unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField( max_length=30)
    date_of_birth = models.DateField( null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField( max_length=1, choices=gender_choices, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    
