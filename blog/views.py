from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post


def add_comment(request):
    """
    A view that display comment to a specific post
    """
    post = get_object_or_404(Post, pk=title)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            Comment.objects.create(
                user=user,
                post=get_object_or_404(Post, pk=title),
                content=content,
            )
            messages.success(request, "Your comment was successfuly added.")
            return redirect(reverse("blog"))
        else:
            messages.error(
                request,
                "Failed to add comment. \
                    Please check the form is valid and try again.",
            )
    else:
        form = CommentForm()
    template = "blog/add_comment.html"
    context = {
        "form": form,
        "post": post,
    }

    return render(request, template, context)
