from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    Title = models.CharField(max_length=250)
    Caption = models.CharField(max_length=500)
    File = models.FileField(upload_to="profile/photos/",null=True)
    like = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return self.Caption


class Comment(models.Model):
    # image = models.ForeignKey(Post, on_delete=models.CASCADE)
    # user = models.ManyToManyField(User)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE, default=0)
    content = models.TextField(max_length= 660, default="Hello")
    # timestamp = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
        # return '{}-{}'.format(self.Post.Title,str(self.user.name))
