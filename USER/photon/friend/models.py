from django.db import models
from main.models import User

# Create your models here.

class Friend(models.Model):
	#user = models.ForeignKey(User)
	users = models.ManyToManyField(User, related_name="friends")
	current_user = models.ForeignKey(User, related_name='owner', null=True)

   





