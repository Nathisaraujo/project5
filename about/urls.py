from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('edit/', views.edit_about_me, name='edit_about_me'),
    path('summernote/', include('django_summernote.urls')),
]
