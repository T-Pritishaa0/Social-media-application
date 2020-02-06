from django import forms

from .models import Post

class OurForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('Title', 'Caption', 'File')

# class CommentForm(forms.ModelForm):
# 	class Meta:
# 		model = Comment
# 		fields = ('content',)
			