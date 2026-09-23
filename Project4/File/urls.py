from django.urls import path 
from . import views

urlpatterns = [
    path('upload/', views.upload_profile, name='upload_profile'),
    path('profile/', views.view_profile, name='view_profile'),
    path('post/', views.post, name='post'),
    path('post_list/', views.post_list, name='post_list')
]
