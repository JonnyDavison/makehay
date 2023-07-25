from django.shortcuts import render

# Create your views here.

def index(request):
    """ a view to retuern the index page """
    return render(request, 'home/index.html')


def ourchef(request):
    """ a view to retuern the index page """
    return render(request, 'home/our-chef.html')

def ourservices(request):
    """ a view to retuern the index page """
    return render(request, 'home/our-services.html')

def letstalk(request):
    """ a view to retuern the index page """
    return render(request, 'home/lets-talk.html')
