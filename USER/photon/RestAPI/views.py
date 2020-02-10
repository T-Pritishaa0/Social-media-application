from django.shortcuts import render
# Create your views here.
from django.db import models
from datetime import datetime 
from django.utils import timezone
from django.apps import apps
from post.models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

# Create your views here.

def api_get_data(request):
    pos = Post.objects.all()
    dict_value = {"Posts": list(pos.values("Title","Caption", "File"))}
    return JsonResponse(dict_value)

def api_spec_data(request, pk = None):
    pos = Post.objects.get(pk = pk)
    return JsonResponse({"Title": pos.Title, "Caption" : pos.Caption})

@csrf_exempt
def api_add(request):
    pos = Post()	
    if request.method == "POST":
        print("hey")
        decoded_data = request.body.decode('utf-8')
        pos_data = json.loads(decoded_data)
        pos.title = pos_data['Title']
        pos.caption = pos_data['Caption']
        user = User.objects.get(first_name="irvin")
        print(user)
        Post.objects.create(Title = title, Caption = caption, user=user)
        return JsonResponse({"message" : "Completed"})
    else:
        return JsonResponse({"Title" : pos.Title, "Caption" : pos.Caption})

@csrf_exempt
def api_update(request, pk = None):
    Pos = Post.objects.get(pk = pk)
    if request.method == "PUT":
        decoded_data = request.body.decode('utf-8')
        Pos_data = json.loads(decoded_data)
        Pos.Title = Pos_data['Title']
        Pos.Caption = Pos_data['Caption']
        Pos.save()
        return JsonResponse({"message" : "Updated"})
    else:
        return JsonResponse({"Title" : Pos.Title, "Caption" : Pos.Caption})

@csrf_exempt
def api_delete(request, pk = None):
    Pos = Post.objects.get(pk = pk)
    if request.method == "DELETE":
        Pos.delete()
        return JsonResponse({"message" : "Deleted"})
    else:
        return JsonResponse({"Title" : Pos.Title, "Caption" : Pos.Caption})

def api_Photon_pagination(request, PAGENO):
    SIZE = 2
    skip = SIZE*(PAGENO-1)
    pos = Post.objects.all()[skip:PAGENO*SIZE]
    dict = {"Posts":list(pos.values("Title","Caption"))}
    return JsonResponse(dict)





























































    
	