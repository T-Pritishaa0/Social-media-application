from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

from . import views 

app_name = "Main"

urlpatterns = [
    path('', views.search, name = "search"),
    path('user/', views.list_Users, name = "list"),
]
