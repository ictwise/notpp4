from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from django.urls import reverse_lazy, reverse


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'


class AddCommentView(CreateView):
    model = Comment
    template_name = 'blog/add_comment.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']

        return super().form_valid(form)

    success_url = reverse_lazy('blog')
