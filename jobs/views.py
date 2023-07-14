from django.shortcuts import render, get_object_or_404
from .models import Roles
# Create your views here.


def all_roles(request):
    """ A view to retuern the roles with sort and search """
    roles = Roles.objects.all()

    context = {
        'roles': roles,
    }

    return render(request, 'jobs/jobs.html', context)


def role_detail(request, job_id):
    """ a view to retuern individual products """
    role = get_object_or_404(Roles, pk=job_id)

    context = {
        'role': role,
    }

    return render(request, 'jobs/jobs_detail.html', context)
