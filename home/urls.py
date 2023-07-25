from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('ourchef/', views.ourchef, name='ourchef'),
    path('ourservices/', views.ourservices, name='ourservices'),
    path('letstalk/', views.letstalk, name='letstalk'),    
]
