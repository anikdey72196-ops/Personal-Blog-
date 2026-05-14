from django.utils import timezone
from django.db import models 

class Profile(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    conform_password = models.CharField(max_length=100)

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True, null=True)
    content = models.TextField(max_length=5000)




# Create your models here.
