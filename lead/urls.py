from django.urls import path

from . import views

urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('detail/<int:pk>/', views.lead_detail, name='lead_detail'),
    path('delete/<int:pk>/', views.lead_delete, name='lead_delete'),
    path('edit/<int:pk>/', views.lead_update, name='lead_edit'),
    path('add-lead/', views.add_lead, name='add_lead'),
]