from django.urls import path
from . import views

urlpatterns = [
    path('', views.personalised_page, name='personalised'),
    # path('product/<int:product_id>/', views.personalised_product_detail, name='personalised_product_detail'),
    # path('process_order/', views.process_order, name='process_order'),
] 