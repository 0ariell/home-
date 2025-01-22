from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo CustomUser.
    Convierte instancias del modelo en JSON y valida datos al crear/actualizar.
    """
    # Campo adicional para mostrar nombre completo (si aplica)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'is_active', 'is_staff', 'full_name']
        read_only_fields = ['id', 'is_active', 'is_staff']  # Campos de solo lectura

    def get_full_name(self, obj):
        """
        Devuelve el nombre completo del usuario si está definido.
        """
        return f"{obj.first_name} {obj.last_name}".strip()

    def validate_email(self, value):
        """
        Validación personalizada para el campo 'email'.
        Verifica que el correo sea único.
        """
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está registrado.")
        return value
