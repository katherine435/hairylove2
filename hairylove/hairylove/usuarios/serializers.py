from rest_framework import serializers
from .models import Usuario, Propietario, Criador


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario', 'nombre', 'apellido', 'correo', 'telefono', 
                  'direccion', 'tipo', 'foto_perfil', 'fecha_nacimiento']
        read_only_fields = ['idUsuario']


class PropietarioSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True)
    
    class Meta:
        model = Propietario
        fields = ['idPropietario', 'user', 'Cantidad_Mascotas', 
                  'Preferencia_Mascota', 'Fecha_Ultima_Adopcion']
        read_only_fields = ['idPropietario', 'Fecha_Registro']


class CriadorSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True)
    
    class Meta:
        model = Criador
        fields = ['idCriador', 'user', 'Razon_Dar_Adopcion', 
                  'Condiciones_Adopcion', 'Tipo_Criador', 
                  'Estado_Verificacion', 'Fecha_Registro']
        read_only_fields = ['idCriador', 'Fecha_Registro']
