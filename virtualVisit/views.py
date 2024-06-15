import requests
from django.shortcuts import render

from museums.settings import SI_API_KEY

# Create your views here.


def index(request):
    context = {}
    return render(request, 'virtualVisit/index.html', context)


def images(requests):
    # Get data from the Smithsonian API
    # More research needed
    return