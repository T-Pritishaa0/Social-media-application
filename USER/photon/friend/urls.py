from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import views

app_name = "friend"

urlpatterns = [
	url(r'^$', FriendView.as_view(), name ='friend')
	url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
	]