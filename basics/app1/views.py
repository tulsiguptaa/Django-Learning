from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("APP1 HOME PAGE")
# Create your views here.
