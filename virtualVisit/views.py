from django.shortcuts import render

from museums.settings import SI_API_KEY

# Create your views here.


def index(request):
    return render(request, 'virtualVisit/index.html')


