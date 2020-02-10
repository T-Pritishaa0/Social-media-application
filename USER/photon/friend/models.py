from django.conf import settings
from django.db import models
from main.models import User

# Create your models here.

class Friend(models.Model):
    users = models.ManyToManyField(User, related_name="friends")
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
    #status = models.CharField(max_length=20, default='requested')
