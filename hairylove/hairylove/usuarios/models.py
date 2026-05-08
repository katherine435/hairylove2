from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date

class Usuario(AbstractUser):

    TIPOS_USUARIO = [
        ('Propietario', 'Propietario'),
        ('Criador', 'Criador'),
    ]

    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    correo = models.EmailField(unique=True,max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    foto_perfil = models.ImageField(upload_to='perfiles/')
    tipo_identificacion = models.CharField(max_length=50)
    numero_identificacion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPOS_USUARIO)
    
    # Campos de calificación
    puntuacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_calificaciones = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.tipo}"

class Criador(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    TIPO_CRIADOR_CHOICES = [
        ('Refugio', 'Refugio'),
        ('Particular', 'Particular'),
        ('Protectora', 'Protectora'),
    ]

    ESTADO_VERIFICACION_CHOICES = [
        ('Verificado', 'Verificado'),
        ('Pendiente', 'Pendiente'),
        ('Rechazado', 'Rechazado'),
    ]

    idCriador = models.AutoField(primary_key=True)
    Razon_Dar_Adopcion = models.TextField(blank=True)
    Condiciones_Adopcion = models.TextField(blank=True)
    Informacion_Rescate = models.TextField(blank=True)
    Tipo_Criador = models.CharField(max_length=20, choices=TIPO_CRIADOR_CHOICES, default='Particular')
    Nombre_Refugio = models.CharField(max_length=200, blank=True)
    Estado_Verificacion = models.CharField(max_length=10, choices=ESTADO_VERIFICACION_CHOICES, default='Pendiente')
    Fecha_Registro = models.DateField(default=date.today)

    def __str__(self):
        return f"Criador {self.idCriador} - {self.Tipo_Criador}"


class Propietario(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    idPropietario = models.AutoField(primary_key=True)
    Cantidad_Mascotas = models.PositiveIntegerField(default=0)
    Fecha_Registro = models.DateField(default=date.today)
    Preferencia_Mascota = models.CharField(max_length=100, null=True, blank=True)
    Fecha_Ultima_Adopcion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Propietario {self.idPropietario} - {self.Cantidad_Mascotas} mascotas"


# ==================== MODELO PARA RESET DE CONTRASEÑA ====================

import uuid
from django.utils import timezone

class PasswordResetToken(models.Model):
    """Modelo para almacenar tokens de reset de contraseña"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='password_reset_tokens')
    token = models.CharField(max_length=255, unique=True, default=uuid.uuid4)
    codigo = models.CharField(max_length=6, null=True, blank=True)  # Código de 6 dígitos
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    used = models.BooleanField(default=False)
    used_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Reset token para {self.user.correo}"
    
    def is_valid(self):
        """Verifica si el token es válido (no expirado y no usado)"""
        return not self.used and timezone.now() < self.expires_at
    
    def mark_as_used(self):
        """Marca el token como utilizado"""
        self.used = True
        self.used_at = timezone.now()
        self.save()


# ==================== MODELO PARA FAVORITOS ====================

class Favorito(models.Model):
    """Modelo para guardar mascotas y servicios favoritos"""
    TIPO_CONTENIDO = [
        ('mascota', 'Mascota'),
        ('servicio', 'Servicio'),
    ]
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favoritos')
    tipo_contenido = models.CharField(max_length=20, choices=TIPO_CONTENIDO)
    id_contenido = models.PositiveIntegerField()  # ID de mascota o servicio
    nombre_contenido = models.CharField(max_length=200)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('usuario', 'tipo_contenido', 'id_contenido')
        ordering = ['-fecha_agregado']
    
    def __str__(self):
        return f"{self.usuario.nombre} - {self.nombre_contenido}"