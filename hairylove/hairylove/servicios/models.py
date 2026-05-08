from django.db import models
from usuarios.models import Usuario
from adopcion.models import Mascota
from datetime import datetime, timedelta

class Servicio(models.Model):
    """Modelo para servicios veterinarios y de cuidado de mascotas"""
    
    TIPO_SERVICIO_CHOICES = [
        ('Consulta General', 'Consulta General'),
        ('Vacunación', 'Vacunación'),
        ('Esterilización', 'Esterilización'),
        ('Castración', 'Castración'),
        ('Cirugía General', 'Cirugía General'),
        ('Limpieza Dental', 'Limpieza Dental'),
        ('Baño y Aseo', 'Baño y Aseo'),
        ('Corte de Pelo', 'Corte de Pelo'),
        ('Desparasitación', 'Desparasitación'),
        ('Análisis Clínico', 'Análisis Clínico'),
        ('Radiografía', 'Radiografía'),
        ('Ecografía', 'Ecografía'),
        ('Seguimiento Posadopción', 'Seguimiento Posadopción'),
        ('Asesoría Comportamiento', 'Asesoría Comportamiento'),
    ]

    idServicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)
    tipo_servicio = models.CharField(max_length=50, choices=TIPO_SERVICIO_CHOICES, default='Consulta General')
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    comision = models.DecimalField(max_digits=5, decimal_places=2, default=15)  # % de comisión
    
    especialista = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='servicios'
    )
    
    duracion_estimada = models.PositiveIntegerField(default=30, help_text="Duración en minutos")
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(null=True, blank=True)
    
    # NUEVOS CAMPOS
    foto_servicio = models.ImageField(upload_to='servicios/', null=True, blank=True)
    puntuacion = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Rating 0-5
    numero_solicitantes = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['tipo_servicio', 'nombre_servicio']

    def __str__(self):
        return f"{self.nombre_servicio} - ${self.precio_base}"


class SolicitudServicio(models.Model):
    """Modelo para solicitudes de servicios"""
    
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Confirmada', 'Confirmada'),
        ('En Progreso', 'En Progreso'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
    ]

    idSolicitud = models.AutoField(primary_key=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, related_name='solicitudes')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='servicios_solicitados')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mis_solicitudes_servicio')
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_programada = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    
    descripcion_problema = models.TextField(blank=True)
    observaciones_especialista = models.TextField(blank=True)
    
    precio_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_completado = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-fecha_solicitud']
    
    def __str__(self):
        return f"{self.servicio.nombre_servicio} - {self.usuario.nombre} ({self.estado})"
    
    def marcar_completada(self):
        """Marcar la solicitud como completada"""
        from django.utils.timezone import now
        self.estado = 'Completada'
        self.fecha_completado = now()
        self.save()
    
    def calcular_precio_final(self, precio_adicional=0):
        """Calcular el precio final con comisión"""
        subtotal = self.servicio.precio_base + precio_adicional
        comision = subtotal * (self.servicio.comision / 100)
        return subtotal - comision


class RespuestaDiagnostico(models.Model):
    """Modelo para almacenar diagnósticos y respuestas del especialista"""
    
    idRespuesta = models.AutoField(primary_key=True)
    solicitud = models.OneToOneField(SolicitudServicio, on_delete=models.CASCADE, related_name='diagnostico')
    especialista = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='diagnosticos')
    
    diagnóstico = models.TextField()
    tratamiento_recomendado = models.TextField()
    medicinas_recomendadas = models.TextField(blank=True)
    proxima_cita = models.DateField(null=True, blank=True)
    
    fecha_diagnostico = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Diagnóstico - {self.solicitud.mascota.Nombre_Mascota}"

