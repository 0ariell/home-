from django.urls import path
from . import views

urlpatterns = [
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
