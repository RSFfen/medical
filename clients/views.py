from django.shortcuts import render

from .models import Client

def index(request) :
    cclients = Client.objects.all()
    return render(request, 'clients/index.html', {'cclients' : cclients })
