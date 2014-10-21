from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
    return HttpResponse("HELLO WORLD")
