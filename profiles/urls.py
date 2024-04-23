from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('recommend/', views.recommend, name='recommend'),
    path('recommendation/success/', views.recommendation_success, name='recommendation_success'),
    path('update_profile/', views.update_profile, name='update_profile'),
]