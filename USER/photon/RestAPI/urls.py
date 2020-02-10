from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "RestAPI"

urlpatterns = [
    path('api/',views.api_get_data, name = "api_get_data"),
    path('api/<int:pk>',views.api_spec_data, name = "api_spec_data"),
    path('api/add/',views.api_add, name = "api_add"),
    path('api/update/<int:pk>',views.api_update,name = "api_update"),
    path('api/delete/<int:pk>',views.api_delete ,name = "api_delete"),
    path('api/page/<int:PAGENO>/', views.api_Photon_pagination, name = "api_Photon_pagination"),
]