from django.urls import path
from .views import BlogView
from . import views

urlpatterns = [
    path('blog/', views.BlogView, name="blog"),
]
