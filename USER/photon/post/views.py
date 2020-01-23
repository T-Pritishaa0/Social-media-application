from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound

from .forms import OurForm
from .models import Post, Comment
from django.contrib.auth.models import User


def upload_file(request):
	form = OurForm()
	if request.method == "POST":
		form = OurForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('post:list')
	return render(request, "post/upload.html",
		{"form":form})

def update_file(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = OurForm()
	if request.method == "POST":
		form = OurForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('post:list')
	return render(request, "post/upload.html", {"form": form})

		

def list_file(request):
	profile = Post.objects.all()
	return render(request, "post/file_list.html",
		{"profiles" : profile})
	
def delete_file(request, pk = None):
	profile = Post.objects.get(pk=pk)
	profile.delete()
	return redirect('post:list')

def post_detail(request, id, slug):
	image = get_object_or_404(Post, id=id, slug=slug)
	comments = Comment.objects.filter(image=image).order_by('-id')

	if request.method == "POST":
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid:
			content = request.POST.get('content')
			Comment.objects.create(image=image, user=request.user, content=content)
			comment.save()
			return HttpResponseRedirect(image.get_absolute_url())
	else:
		comment_form= CommentForm()

	context = {
		'image' : image,
		'comments': comments,
		'comment_form': comment_form,

	}

	return render(request, "post/file_list.html", context)

 
