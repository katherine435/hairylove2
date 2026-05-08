from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.principal, name='index'),
    path('login/', views.inicio_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('registro/', views.registro, name='registro'),
    
    # Rutas de perfil (CORRECTAS)
    path('perfil-propietario/', views.perfil_propietario, name='propietario'),
    path('perfil-criador/', views.perfil_criador, name='criador'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    
    # Otras rutas
    path('actualizar-foto/', views.actualizar_foto, name='actualizar_foto'),
    path('formulario-servicios/', views.formularioServicios, name='formularioServicios'),
    path('mascotas-adopcion/', views.mascotas_adopcion, name='mascotas_adopcion'),
    
    # Rutas para recuperación de contraseña con código
    path('solicitar-reset-contrasena/', views.solicitar_reset_contrasena, name='solicitar_reset_contrasena'),
    path('verificar-codigo/', views.verificar_codigo_reset, name='verificar_codigo_reset'),
    path('reset-contrasena/<str:token>/', views.reset_contrasena, name='reset_contrasena'),  # Retrocompatibilidad
    
    # Rutas para favoritos
    path('toggle-favorito/', views.toggle_favorito, name='toggle_favorito'),
    path('mis-favoritos/', views.mis_favoritos, name='mis_favoritos'),
    
    # Rutas para estadísticas
    path('estadisticas-calificaciones/', views.estadisticas_calificaciones, name='estadisticas_calificaciones'),
    
    # Rutas para notificaciones
    path('notificaciones/', views.notificaciones, name='notificaciones'),
    path('notificaciones/marcar-todas/', views.marcar_todas_notificaciones, name='marcar_todas_notificaciones'),
]