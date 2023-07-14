from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_roles, name='roles'),
    path('<job_id>', views.role_detail, name='role_detail'),
]
