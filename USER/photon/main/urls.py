from django.urls import path 
from django.conf.urls import url
from . import views


urlpatterns = [
    #path("register", views.register, name="register"),
    url(r'^$', views.index),
    url(r'^register/$', views.register, name="register"),
   # path('home',views.home, name='home'),
   
    ]
