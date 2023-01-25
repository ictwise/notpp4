from django.urls import path
from .views import PostListView, PostDetailView, AddPostView, AddCommentView


urlpatterns = [
    path('blog/', PostListView.as_view(), name="blog"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('blog/add_post/', AddPostView.as_view(), name="add_post"),
    path('blog/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    ]
