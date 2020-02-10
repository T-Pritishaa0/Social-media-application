from django.db import models
from datetime import datetime 
from django.utils import timezone
from django.apps import apps

class User(models.Model):
	first_name = models.CharField(max_length=200) 
	last_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200) 
	password = models.CharField(max_length=200)
   # dob = models.DateField() 
   # gender = models.CharField(max_length=20)
    #age = models.IntegerField()
# Create your models here.

