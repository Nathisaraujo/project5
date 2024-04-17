from django.urls import path
from . import views

urlpatterns = [
    path('', views.personalised_page, name='personalised'),
] 