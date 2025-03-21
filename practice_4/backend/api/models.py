from django.db import models 
from django.contrib.auth.models import AbstractUser, Group, Permission  

class Item(models.Model): 

    name = models.CharField(max_length=100) 

    description = models.TextField()  

class User(AbstractUser): 

    ROLE_CHOICES = [ 

        ('admin', 'Admin'), 

        ('user', 'User'), 

    ] 

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user') 
    groups = models.ManyToManyField(
        Group,
        related_name="api_user_set",  # ✅ Custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="api_user_permissions_set",  # ✅ Custom related_name
        blank=True
    )