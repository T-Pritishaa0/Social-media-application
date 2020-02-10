
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


app_name = "Main"

urlpatterns = [
    #path("register", views.register, name="register"),
    url(r'^$', views.index),
    #3url(r'^register/$', views.register, name="register"),
    # path('home',views.home, name='home'),
    path('Nav/', views.search, name = "search"),
    path('user/', views.list_Users, name = "list"),
]

