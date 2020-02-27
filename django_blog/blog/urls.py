from django.urls import path
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),  # first url mapped
    path('', PostListView.as_view(), name='blog-home'),  # first url mapped
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # first url mapped
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # first url mapped
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
