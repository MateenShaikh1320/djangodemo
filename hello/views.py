from django.shortcuts import render
from django.http import HttpResponse

def sayhello(request):
    return HttpResponse("<h2> Welcome! This is a Django demo project deployed on a DigitalOcean droplet running Ubuntu 20.04 64 bit LTS server using nginx and gunicorn </h2>")
