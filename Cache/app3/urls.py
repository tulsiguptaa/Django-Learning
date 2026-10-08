from django.urls import path
from .views import db_cache

urlpatterns = [
    path('db-cache/', db_cache, name="db_cache"),
]