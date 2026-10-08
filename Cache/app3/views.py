from django.shortcuts import render
from .models import User
from django.core.cache import cache
# Create your views here.
def db_cache(request):
    user = cache.get('db_cache')
    return render(request, 'home.html')