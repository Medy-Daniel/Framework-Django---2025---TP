from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('events/', views.events_list, name='events_list'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
]
