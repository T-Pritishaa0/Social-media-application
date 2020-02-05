from django.shortcuts import render
from django.db import models
from datetime import datetime 
from django.utils import timezone
from django.apps import apps
from django .models import * 
from django.http import HttpResponse, JsonResponse
import django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def api_get_data(request):
    User = User.objects.all()
    dict_value = {"Users": list(User.values("first_name","last_name", "email"))}
    return JsonResponse(dict_value)

def api_spec_data(request, pk = None):
    User = User.objects.get(pk = pk)
    return JsonResponse({"first_name": User.first_name, "last_name" : User.last_name, "email" : User.email})

@csrf_exempt
def api_add(request):
    user = User()
    if request.method == "POST":
        decoded_data = request.body.decode('utf-8')
        User_data = json.loads(decoded_data)
        User.email = User_data['email']
        User.first_name = User_data['first_name']
        User.last_name = User_data['last_name']
        User.save()
        return JsonResponse({"message" : "Completed"})
    else:
        return JsonResponse({"email" : User.email, "first_name" : User.first_name, "last_name" : User.last_name})

@csrf_exempt
def api_update(request, pk = None):
    User = User.objects.get(pk = pk)
    if request.method = "PUT":
        decoded_data = request.body.decode('utf-8')
        User_data = json.loads(decoded_data)
        User.email = User_data['email']
        User.first_name = User_data['first_name']
        User.last_name = User_data['last_name']
        User.save()
        return JsonResponse({"message" : "Updated"})
    else:
        return JsonResponse({"email" : User.email, "first_name" : User.first_name, "last_name" : User.last_name})

@csrf_exempt
def api_delete(request, pk = None):
    User = User.objects.get(pk = pk)
    if request.method == "DELETE":
        User.delete()
        return JsonResponse{("message" : "Deleted")}
    else:
        return JsonResponse({"email" : User.email, "first_name" : User.first_name, "last_name" : User.last_name})
