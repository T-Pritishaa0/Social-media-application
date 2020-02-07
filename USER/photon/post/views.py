from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseNotFound

from .forms import OurForm
from .models import Post, Comment
from django.contrib.auth.models import User


def upload_file(request):
	form = OurForm()
	if request.method == "POST":

		form = OurForm(request.POST, request.FILES)
		print(request.POST)
		print(request.FILES)
		print(form['Title'])
		if form.is_valid():
			print("I am here")
			title = form.cleaned_data['Title']
			caption= form.cleaned_data['Caption']
			file = form.cleaned_data['File']
			Post.objects.create(Title =title,Caption =caption,File=file,user_id=request.user.id)
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
	context = []
	posts = Post.objects.all()
	for post in posts:
		comments = []
		comment_collection =Comment.objects.filter(post = post.id)
		for comment in comment_collection:
			comments.append(comment.content)
		print(post.File.url)
		context.append({"pk": post.pk,
						"title": post.Title,
						"caption": post.Caption,
						"url": post.File.url,
						"likes": post.like,
						"comments": comments})
	
	return render(request, "post/file_list.html",
		{"profiles" : context})
	# return JsonResponse({"profiles" : context})
	
def delete_file(request, pk = None):
	profile = Post.objects.get(pk=pk)
	profile.delete()
	return redirect('post:list')

'''def post_detail(request, id, slug):
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

	return render(request, "post/file_list.html", context)'''

 
def comment(request,id):
	if request.method == "POST" and request.POST['comment']:
		comment = request.POST['comment']
		post_id = Post.objects.get(id=id)
		new_comment = Comment.objects.create(post=post_id,content=comment)
		return redirect('post:list')
	return render(request, "post/comment.html", {"form": form})

def like(request,id):
	if request.method == "POST":
		post_id = Post.objects.get(id=id)
		post_id.like += 1
		post_id.save()
		return redirect('post:list')
	return render(request, "post/error.html")