from django.urls import path

from . import views


urlpatterns = [
    path('', views.client_list, name='clients_list'),
    path('detail/<int:pk>/', views.client_detail, name='client_detail'),
    path('update/<int:pk>/', views.update_client, name='client_update'),
    path('delete/<int:pk>/', views.delete_client, name='client_delete'),
    path('add/', views.add_client, name='add_client'),
    
]