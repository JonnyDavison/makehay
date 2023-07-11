from django.shortcuts import render
from .models import Roles
# Create your views here.

def all_roles(request):
    """ a view to retuern the products with sort and serch """
    roles = Roles.objects.all()

    context = {
        'roles': roles,
    }

    return render(request, 'jobs/jobs.html', context)
