from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def set_session(request):
    request.session['username'] = 'tulsi'
    request.session['course'] = 'django'
    return HttpResponse("Saved")

def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'Not enrolled')
    return HttpResponse(f"Welcome {username} {course}")

def delete_session(request):
    request.session.flush()
    return HttpResponse("Deleted")

def set_cookies(request):
    response = HttpResponse("cookies set")
    response.set_cookie('username', 'tulsi gupta', max_age=60*60*24)
    return response

def get_cookies(request):
    username = request.COOKIES.get('username', 'Guest')
    return HttpResponse(f"Username : {username}")

def delete_cookies(request):
    response = HttpResponse("cookie deleted")
    response.delete_cookie('username')
    return response