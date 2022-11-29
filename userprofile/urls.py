from django.urls import path
from django.contrib.auth import views
from .views import signup

urlpatterns = [
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login' ),
    path('log-out', views.LogoutView.as_view(), name='logout'),
]
