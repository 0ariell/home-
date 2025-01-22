from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin
    path('usuarios/', include('usuarios.urls')),  # Incluye las rutas de usuarios
]
