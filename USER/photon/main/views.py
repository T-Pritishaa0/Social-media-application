from django.shortcuts import render
from .models import User
from django.db.models import Q

# Create your views here.

def list_Users(request):
    query = " "
    context = {}
    if request.GET:
        query = request.GET['q']
    book = get_data_queryset(query)
    context['Users'] = book
    return render(request, "personal/Search.html",
        {"Users" : User})

def get_data_queryset(query = None):
    queryset= []
    queries = query.split(" ")
    for q in queries:
        Users = Users.objects.filter(
            Q(title__icontains = q) |
            Q(name__icontains = q)
            )

        for User in Users:
            queryset.append(User)

    return list(set(queryset))
        