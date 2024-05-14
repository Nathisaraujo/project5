from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('recommend/', views.recommend, name='recommend'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('orders/', views.orders, name='orders'),
    path('saved_events/', views.saved_events, name='saved_events'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('management/', views.management, name='management'),
]