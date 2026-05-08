from django.contrib import admin
from .models import Servicio, SolicitudServicio, RespuestaDiagnostico

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'tipo_servicio', 'precio_base', 'especialista', 'disponible')
    list_filter = ('tipo_servicio', 'disponible', 'fecha_creacion')
    search_fields = ('nombre_servicio', 'especialista__nombre')
    readonly_fields = ('fecha_creacion',)

@admin.register(SolicitudServicio)
class SolicitudServicioAdmin(admin.ModelAdmin):
    list_display = ('idSolicitud', 'servicio', 'mascota', 'usuario', 'estado', 'fecha_programada')
    list_filter = ('estado', 'fecha_programada')
    search_fields = ('mascota__Nombre_Mascota', 'usuario__correo', 'servicio__nombre_servicio')
    readonly_fields = ('fecha_solicitud', 'fecha_completado')

@admin.register(RespuestaDiagnostico)
class RespuestaDiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('idRespuesta', 'solicitud', 'especialista', 'fecha_diagnostico')
    list_filter = ('fecha_diagnostico',)
    search_fields = ('solicitud__mascota__Nombre_Mascota', 'especialista__nombre')
    readonly_fields = ('fecha_diagnostico',)
