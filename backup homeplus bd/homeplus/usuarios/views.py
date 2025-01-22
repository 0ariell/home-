from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import JsonResponse
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Acceso permitido solo para usuarios autenticados'})


@api_view(['POST'])
def login_api(request):
    """
    API para autenticar a un usuario mediante JSON y devolver un token JWT.
    """
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'success': False, 'message': 'Correo electrónico o contraseña faltante'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=email, password=password)
    if user is not None:
        # Generar el token JWT
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'success': True, 'message': 'Login exitoso', 'access_token': access_token})
    else:
        return Response({'success': False, 'message': 'Credenciales incorrectas'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_api(request):
    """
    API para autenticar a un usuario mediante JSON.
    """
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'success': False, 'message': 'Correo electrónico o contraseña faltante'}, status=400)

    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({
            'success': True,
            'message': 'Login exitoso',
            'access_token': str(refresh.access_token),  # Token de acceso
        })
    else:
        return Response({'success': False, 'message': 'Credenciales incorrectas'}, status=400)


# Vista para la página principal (home)
def home(request):
    """
    Renderiza la página principal.
    """
    return render(request, 'home.html')  # Cambia 'home.html' por tu plantilla de inicio


# API para registrar usuarios
@api_view(['POST'])
def register(request):
    """
    API para registrar un nuevo usuario.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Usuario registrado exitosamente'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Lista de usuarios (API)
class UserList(APIView):
    """
    API para listar y registrar usuarios.
    """
    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
