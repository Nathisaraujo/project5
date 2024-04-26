from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/like/', views.like_posts.as_view(), name='like_post'),
    
] 