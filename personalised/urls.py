from django.urls import path
from . import views

urlpatterns = [
    path('', views.personalised_page, name='personalised'),
    # path('order/', views.order_page, name='order'),
    path('personalised/order/', views.personalised_order, name='personalised_order'),
] 