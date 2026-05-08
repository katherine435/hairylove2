import re
from django.db import models
from django.utils import timezone

class Mascota(models.Model):
    GENERO_CHOICES = [
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    ]

    ORIGEN_CHOICES = [
        ('Criador', 'Criador'),
        ('Refugio', 'Refugio'),
        ('Rescate', 'Rescate'),
        ('Abandono', 'Abandono'),
    ]

    ESTADO_SALUD_CHOICES = [
        ('Excelente', 'Excelente'),
        ('Buena', 'Buena'),
        ('Regular', 'Regular'),
       
    ]

    TAMAÑO_CHOICES = [
        ('Pequeño', 'Pequeño'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]

    TAMAÑO_CHOICES = [
        ('Pequeño', 'Pequeño'),
        ('Mediano', 'Mediano'),
        ('Grande', 'Grande'),
    ]

    idMascota = models.AutoField(primary_key=True)
    Nombre_Mascota = models.CharField(max_length=100)
    Fecha_Nacimiento = models.DateField()
    Raza = models.CharField(max_length=100)
    Genero = models.CharField(max_length=6, choices=GENERO_CHOICES)
    Peso = models.FloatField()
    Especie = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Tamaño = models.CharField(max_length=50, choices=TAMAÑO_CHOICES)
    Historial_Mascota = models.TextField()
    Origen = models.CharField(max_length=10, choices=ORIGEN_CHOICES, default='Criador')
    Tipo_Alimentación = models.CharField(max_length=100)
    Enfermedades = models.TextField()
    Vivienda = models.CharField(max_length=100)
    Vacunas = models.TextField()
    Compatibilidad_Mascota = models.TextField()
    Descripción_Física = models.TextField()
    idCriador = models.IntegerField(null=True, blank=True)
    Estado_Salud = models.CharField(max_length=10, choices=ESTADO_SALUD_CHOICES, default='Buena')
    Esterilizado = models.BooleanField(default=False)
    Socializado = models.BooleanField(default=True)
    
    # NUEVOS CAMPOS
    foto_mascota = models.ImageField(upload_to='mascotas/', null=True, blank=True)
    disponible = models.BooleanField(default=True)
    puntuacion = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Rating 0-5
    numero_personas_interesadas = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)

    @property
    def nombre_limpio(self):
        return re.sub(r'\s+\d+$', '', self.Nombre_Mascota).strip()

    def __str__(self):
        return self.Nombre_Mascota



class Adopcion(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aprobada', 'Aprobada'),
        ('Rechazada', 'Rechazada'),
    ]

    ESTADO_SOLICITUD_CHOICES = [
        ('En revisión', 'En revisión'),
        ('En camino', 'En camino'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
    ]

    FUENTE_MASCOTA_CHOICES = [
        ('Criador', 'Criador'),
        ('Refugio', 'Refugio'),
        ('Rescate', 'Rescate'),
    ]

    idAdopcion = models.AutoField(primary_key=True)
    idPropietario = models.IntegerField()  
    idMascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    idCriador = models.IntegerField(null=True, blank=True)  
    Estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    Fecha_Solicitud = models.DateField()
    Fecha_Adopción = models.DateField()
    Fecha_Entrega = models.DateField()
    Motivo_Adopción = models.TextField()
    Control_Adopción = models.TextField()
    Estado_Salud_Mascota = models.TextField()
    Lugar_Vivienda = models.TextField()
    Info_Mascota = models.TextField()
    Estado_Ingreso_Mascota = models.TextField()
    Devolución = models.TextField()
    Estado_Solicitud = models.CharField(max_length=50, choices=ESTADO_SOLICITUD_CHOICES)
    Motivo_Rechazo = models.TextField(null=True, blank=True)
    Fuente_Mascota = models.CharField(max_length=10, choices=FUENTE_MASCOTA_CHOICES, default='Criador')

    def __str__(self):
        return f"Adopción {self.idAdopcion} - Mascota {self.idMascota.Nombre_Mascota}"


class Calificacion(models.Model):
    
    PUNTUACION_CHOICES = [
        (1, '⭐ 1 - Muy Malo'),
        (2, '⭐⭐ 2 - Malo'),
        (3, '⭐⭐⭐ 3 - Regular'),
        (4, '⭐⭐⭐⭐ 4 - Bueno'),
        (5, '⭐⭐⭐⭐⭐ 5 - Excelente'),
    ]

    idCalificacion = models.AutoField(primary_key=True)
    adopcion = models.ForeignKey(Adopcion, on_delete=models.CASCADE, related_name='calificaciones')
    usuario_califica = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='calificaciones_dadas')
    usuario_calificado = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='calificaciones_recibidas')
    puntuacion = models.IntegerField(choices=PUNTUACION_CHOICES)
    comentario = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Evita que se pueda calificar dos veces la misma adopción de la misma forma
        unique_together = ('usuario_califica', 'usuario_calificado', 'adopcion')
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.usuario_califica.nombre} califica a {self.usuario_calificado.nombre} - {self.puntuacion}⭐"


class Notificacion(models.Model):
    """
    Modelo para almacenar notificaciones de usuarios.
    Se crean cuando alguien recibe una calificación, solicitud de adopción, aprobación o rechazo.
    """
    TIPO_CHOICES = [
        ('calificacion', 'Nueva Calificación'),
        ('solicitud_adopcion', 'Nueva Solicitud de Adopción'),
        ('adopcion_aprobada', 'Adopción Aprobada'),
        ('adopcion_rechazada', 'Adopción Rechazada'),
    ]
    
    idNotificacion = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='notificaciones')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, default='calificacion')
    adopcion = models.ForeignKey(Adopcion, on_delete=models.CASCADE, related_name='notificaciones', null=True, blank=True)
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    relacionado_con = models.CharField(max_length=50, null=True, blank=True)  # El ID del objeto relacionado (e.g., idCalificacion)
    leido = models.BooleanField(default=False)
    enlace_accion = models.CharField(max_length=200, null=True, blank=True)  # URL para hacer click en la notificación
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{'[Leído]' if self.leido else '[Nuevo]'} {self.titulo} - {self.usuario.nombre}"

class ChatMessage(models.Model):
    """Mensajes de chat entre Propietario y Criador"""
    idChat = models.AutoField(primary_key=True)
    remitente = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='mensajes_recibidos')
    mensaje = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.remitente.username} -> {self.receptor.username} @ {self.timestamp}"