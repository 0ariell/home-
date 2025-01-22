from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import User

admin.site.register(User)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)