from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length = 140)
    phone = models.CharField(max_length = 15, default='9192939495')
    
    def __str__(self):
        return self.user.username
