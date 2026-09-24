from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreate(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'content']

class PostUpdate(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']

class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')