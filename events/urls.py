from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('save_event/<int:event_id>/', views.save_event, name='save_event'),
    path('unsave/<int:event_id>/', views.unsave_event, name='unsave_event'),
    path('unsave_profile/<int:event_id>/', views.unsave_event_profile, name='unsave_event_profile'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
] 