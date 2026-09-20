from django.shortcuts import render, redirect
from .forms import Form 
from .models import Student,Post
from django.contrib import messages
from django.core.paginator import Paginator

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
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(posts, 1)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'accounts/post.html', {'page_obj' : page_obj})