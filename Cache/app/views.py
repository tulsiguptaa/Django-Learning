from django.shortcuts import render
from .models import User
from django.core.cache import cache

def user_list(request):
    cache.set("username", "naina", 60)
    return render(request,'user.html')
