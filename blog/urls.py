from django.urls import path
from .views import BlogPostView, BlogDetailedView


urlpatterns = [
    path('post/<int:pk>/', BlogDetailedView.as_view(), name='post_detail'),
    path('', BlogPostView.as_view(), name='home'),
]
