from django.shortcuts import render
from .models import Roles
# Create your views here.


def all_roles(request):
    """ A view to retuern the roles with sort and search """
    roles = Roles.objects.all()

    context = {
        'roles': roles,
    }

    return render(request, 'jobs/jobs.html', context)
