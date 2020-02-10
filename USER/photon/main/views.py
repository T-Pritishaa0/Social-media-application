
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import User
from django.db.models import Q

def index(request):
	return render(request, 'index.html')


def home(request):
	return render(request, 'home.html',{'name':'kinju'})


def search(request):
    return render(request = request , template_name = "NAV.html" , context = {})

def list_Users(request):
    u = User.objects.all()
    query = " "
    context = {}
    if request.GET:
        query = request.GET['q']
        u = get_data_queryset(query)
    context['Users'] = u
    return render(request, "list.html",
        context)

def get_data_queryset(query = None):
    queryset= []
    queries = query.split(" ")
    for q in queries:
        Users = User.objects.filter(
            Q(first_name__icontains = q) |
            Q(last_name__icontains = q) |
            Q(email__icontains = q)
            )

        for U in Users:
            queryset.append(U)

    return list(set(queryset))
        

