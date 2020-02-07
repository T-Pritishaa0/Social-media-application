from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

def index(request):
	return render(request, 'index.html')


def home(request):
	return render(request, 'home.html',{'name':'kinju'})


