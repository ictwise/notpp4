from django.shortcuts import render
from .models import Post


def BlogView(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)
   