from django.db import models

class Post(models.Model):
	Title = models.CharField(max_length=100)
	Caption = models.CharField(max_length=100)
	File = models.FileField(upload_to="profile/photos/")

	def __str__(self):
		return self.Title
