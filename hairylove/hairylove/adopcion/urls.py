from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .viewsets import MascotaViewSet, AdopcionViewSet

# Router para APIs RESTful
router = DefaultRouter()
router.register(r'mascotas', MascotaViewSet, basename='mascota')
router.register(r'adopciones', AdopcionViewSet, basename='adopcion')

urlpatterns = [
    # Vistas tradicionales - Adopción
    path('mascotas/', views.mascotas, name='mascotas'),
    path('adoptar/', views.formulario_adopcion, name='formulario_adopcion'),
    path('descargar-reporte/<int:adopcion_id>/', views.descargar_reporte_adopcion, name='descargar_reporte_adopcion'),
    
    # Nuevas vistas para registrar mascotas en adopción
    path('registrar-mascota/', views.registrar_mascota_adopcion, name='registrar_mascota_adopcion'),
    path('mis-mascotas/', views.mis_mascotas_adopcion, name='mis_mascotas_adopcion'),
    path('disponibles/', views.mascotas_adopcion_disponibles, name='mascotas_adopcion_disponibles'),
    path('mascota/<int:mascota_id>/', views.detalles_mascota, name='detalles_mascota'),
    path('mascota/<int:mascota_id>/editar/', views.editar_mascota, name='editar_mascota'),
    path('mascota/<int:mascota_id>/eliminar/', views.eliminar_mascota, name='eliminar_mascota'),
    path('mascota/<int:mascota_id>/solicitudes/', views.ver_solicitudes_mascota, name='ver_solicitudes_mascota'),
    path('solicitar/<int:mascota_id>/', views.solicitar_adopcion, name='solicitar_adopcion'),
    path('mis-adopciones/', views.mis_adopciones, name='mis_adopciones'),
    
    # Vistas para que criadores manejen solicitudes de adopción
    path('solicitudes/', views.solicitudes_adopcion_criador, name='solicitudes_adopcion_criador'),
    path('solicitud/<int:adopcion_id>/aprobar/', views.aprobar_solicitud_adopcion, name='aprobar_solicitud_adopcion'),
    path('solicitud/<int:adopcion_id>/rechazar/', views.rechazar_solicitud_adopcion, name='rechazar_solicitud_adopcion'),
    
    # Vistas para calificaciones
    path('calificar/<int:adopcion_id>/', views.crear_calificacion, name='crear_calificacion'),
    
    # Vistas para chat
    path('chat/', views.chat_lista, name='chat_lista'),
    path('chat/<int:usuario_id>/messages/', views.chat_mensajes_api, name='chat_mensajes_api'),
    path('chat/<int:usuario_id>/', views.chat_mensajes, name='chat_mensajes'),

    # Seguimiento adopción
    path('seguimiento/<int:adopcion_id>/', views.seguimiento_adopcion, name='seguimiento_adopcion'),

    # Admin: Excel de adopciones
    path('excel-adopciones/', views.descargar_excel_adopciones, name='descargar_excel_adopciones'),

    # Generar mascotas falsas
    path('generar-mascotas/', views.crear_adoptar_mascotas_random, name='crear_adoptar_mascotas_random'),

    # Carga masiva de mascotas
    path('carga-masiva/', views.carga_masiva_mascotas, name='carga_masiva_mascotas'),

    # APIs para registro dinámico de mascotas
    path('api/especies/', views.api_especies, name='api_especies'),
    path('api/razas-por-especie/', views.api_razas_por_especie, name='api_razas_por_especie'),
    path('api/generos/', views.api_generos, name='api_generos'),
    path('api/tamanos/', views.api_tamanos, name='api_tamanos'),

    # APIs RESTful
    path('api/', include(router.urls)),
]