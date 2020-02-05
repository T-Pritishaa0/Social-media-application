from django.shortcuts import render
from .models import User
from django.db.models import Q

# Create your views here.

def list_Users(request):
    u = User.objects.all()
    query = " "
    context = {}
    if request.GET:
        query = request.GET['q']
        u = get_data_queryset(query)
    context['Users'] = u
    return render(request, "Search.html",
        context)

def get_data_queryset(query = None):
    queryset= []
    queries = query.split(" ")
    for q in queries:
        Users = User.objects.filter(
            Q(title__icontains = q) |
            Q(name__icontains = q)
            )

        for User in Users:
            queryset.append(User)

    return list(set(queryset))
        