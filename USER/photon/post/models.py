from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	Title = models.CharField(max_length=100)
	Caption = models.CharField(max_length=100)
	File = models.FileField(upload_to="profile/photos/")

	def __str__(self):
		return self.Title


class Comment(models.Model):
    image = models.ForeignKey(Post,blank=True, on_delete=models.CASCADE )
    comment_owner = models.ManyToManyField(User)
    comment = models.TextField()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments

    def __str__(self):
        return str(self.comment)
