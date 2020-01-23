from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	Title = models.CharField(max_length=100)
	Caption = models.CharField(max_length=100)
	File = models.FileField(upload_to="profile/photos/")

	def __str__(self):
		return self.Title


class Comment(models.Model):
    image = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    content = models.TextField(max_length= 160)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}-{}'.format(self.Post.Title,str(self.user.name))
