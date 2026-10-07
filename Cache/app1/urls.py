from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.file_cache, name='user_list'),
]
