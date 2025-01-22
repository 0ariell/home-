from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Registro de usuarios
    path('login/', views.login_view, name='login'),      # Login
    path('home/', views.home, name='home'),             # Página de inicio
    path('users/', views.UserList.as_view(), name='user-list'),  # API de usuarios
]

