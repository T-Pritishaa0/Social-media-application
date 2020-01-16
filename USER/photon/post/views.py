from django.shortcuts import render, redirect

# Create your views here.
from .forms import OurForm
from .forms import Post

def upload_file(request):
	if request.method == "POST":
		form = OurForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('post:list')



	else:
		form = OurForm()
	return render(request, "post/upload.html",
		{"form":form})

		

def list_file(request):
	profile = Post.objects.all()
	return render(request, "post/file_list.html",
		{"profiles" : profile})
	
def delete_file(request, pk = None):
	profile = Post.objects.get(pk=pk)
	profile.delete()
	return redirect('post:list')
