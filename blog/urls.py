from django.urls import path
from .views import BlogView
from . import views

urlpatterns = [
    path('blog/', views.BlogView, name="blog"),
    path("blog/<uuid:pk>/add_comment/", views.add_comment, name="add_comment"),
]
