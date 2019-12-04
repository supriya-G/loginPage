from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Login(models.Model):
    username1=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    