from django.shortcuts import render
from .models import User
from django.core.cache import cache
from django.http import HttpResponse
# Create your views here.

def user_list(request):
    cache.set("username", "naina", 60)
    return render(request,'user.html')

def get_cache_data(request):
    username = cache.get('username')
    return HttpResponse('Username: ', username)

