from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class CustomUser(AbstractUser):
    # username_validator = UnicodeUsernameValidator()
     
    username = None
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=14)
    
    objects = UserManager()
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    
