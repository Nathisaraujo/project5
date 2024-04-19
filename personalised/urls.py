from django.urls import path
from . import views
from .views import PersonalisedOrder

urlpatterns = [
    path('', views.personalised_page, name='personalised'),
    path('order/', PersonalisedOrder.as_view(), name='personalised_order'),
] 