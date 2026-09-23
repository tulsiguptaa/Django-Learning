from django.shortcuts import render, redirect
from .forms import Form 
from .models import Student,Post
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

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
    paginator = Paginator(posts, 1)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'accounts/post.html', {'page_obj' : page_obj})

def post_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    posts = Post.objects.all()

    # search using queries 
    if query:
        posts = Post.filter(
            Q(title_icontains = query) | Q(content_icontains = query)
        )

    if category:
        posts = posts.filter(category_iexact=category)

    return render( request, 'accounts/post_list.html', {'posts': post, 'query': query})