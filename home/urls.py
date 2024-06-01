from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
