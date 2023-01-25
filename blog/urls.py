from django.urls import path
from .views import PostListView, PostDetailView, AddPostView
from . import views

urlpatterns = [
    path('blog/', PostListView.as_view(), name="blog"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('blog/add_post/', AddPostView.as_view(), name="add_post"),
]
