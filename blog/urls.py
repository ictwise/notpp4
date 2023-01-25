from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('blog/', PostListView.as_view(), name="blog"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name="post-detail"),

    path("blog/<uuid:pk>/add_comment/", views.add_comment, name="add_comment"),
]
