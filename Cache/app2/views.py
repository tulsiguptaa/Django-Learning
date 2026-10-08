from django.shortcuts import render
from django.core.cache import caches
from django.http import HttpResponse
from .models import User

def fragment_cache(request):
    file_cache = caches["file_cache"]
    user_list = User.objects.all()
    return render(request, 'welcome.html', {user_list: 'user_list'})
