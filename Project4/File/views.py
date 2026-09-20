from django.shortcuts import render, redirect
from .forms import Form 
from .models import Student,Post
from django.contrib import messages

# Create your views here.
def upload_profile(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture uploaded')
            return redirect('view_profile')
        else:
            messages.error(request, 'Error in upload')
    else:
        form = Form()
        return render(request, 'accounts/upload_profile.html', {'form':form})

def view_profile(request):
    profiles = Student.objects.all()
    return render(request, 'accounts/view_profile.html', {'profiles': profiles})

def post(request):
    posts = Post.objects.all()
    return render(request, 'accounts/post.html', {'posts': posts})