from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Comment
from django.urls import reverse_lazy, reverse
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPostView(UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    def test_func(self):
        return self.request.user.is_superuser


class EditPostView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/edit_post.html'

    def test_func(self):
        return self.request.user.is_superuser


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']

        return super().form_valid(form)

    success_url = reverse_lazy('blog')
