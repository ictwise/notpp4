from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def view_blog(request):
#    return render(request, 'blog/blog.html', {})

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
