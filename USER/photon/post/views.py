from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import OurForm
from .models import Post


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
