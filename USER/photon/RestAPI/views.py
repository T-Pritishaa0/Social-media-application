from django.shortcuts import render
from django.db import models
from datetime import datetime 
from django.utils import timezone
from django.apps import apps
from django .models import * 
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.

def api_get_data(request):
    User = User.objects.all()
    dict_value = {"Users": list(User.values("first_name","last_name", "email"))}
    return JsonResponse(dict_value)

def api_spec_data(request, pk = None):
    User = User.objects.get(pk = pk)
    return JsonResponse({"first_name": User.first_name, "last_name" : User.last_name, "email" : User.email})
    