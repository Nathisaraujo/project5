from django.urls import path
from . import views
from .views import PersonalisedOrder

urlpatterns = [
    path('', views.personalised_page, name='personalised'),
    path('order/', views.PersonalisedOrder, name='personalised_order'),
    path('order-summary/', views.order_summary, name='order_summary'),
] 