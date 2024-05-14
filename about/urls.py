from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('edit/', views.edit_about_me, name='edit_about_me'),
] 