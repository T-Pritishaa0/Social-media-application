from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "post"


urlpatterns = [
	 path('profile/upload/', views.upload_file, name="upload"),
	 path('profile/', views.list_file, name="list"),
	 path('profile/delete/<int:pk>/', views.delete_file, name="delete"),
	 path('profile/<int:id>/', views.update_file, name="update"),
	 path('profile/<int:id>/' views.comment, name="comment"),	
]