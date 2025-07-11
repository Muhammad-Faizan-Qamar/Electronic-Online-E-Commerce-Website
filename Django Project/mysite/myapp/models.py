from django.db import models

# Create your models here.

class UserProfile(models.Model):
    UserName = models.CharField(max_length=30)
    Password = models.IntegerField()
    Email = models.EmailField(max_length=255)
    
class ContactInformation(models.Model):
    Phone = models.IntegerField()
    Address = models.CharField(max_length=250)
    Place = models.TextField()