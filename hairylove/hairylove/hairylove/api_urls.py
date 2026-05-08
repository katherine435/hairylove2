from rest_framework.routers import DefaultRouter
from usuarios.views import UsuarioViewSet, PropietarioViewSet, CriadorViewSet
from servicios.views import ServicioViewSet, SolicitudServicioViewSet
from adopcion.views import MascotaViewSet, AdopcionViewSet
from adopcion.viewsets import CalificacionViewSet, NotificacionViewSet, ChatMessageViewSet

# Crear router
router = DefaultRouter()

# Registrar viewsets de usuarios
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'propietarios', PropietarioViewSet, basename='propietario')
router.register(r'criadores', CriadorViewSet, basename='criador')

# Registrar viewsets de servicios
router.register(r'servicios', ServicioViewSet, basename='servicio')
router.register(r'solicitudes-servicio', SolicitudServicioViewSet, basename='solicitudservicio')

# Registrar viewsets de adopción
router.register(r'mascotas', MascotaViewSet, basename='mascota')
router.register(r'adopciones', AdopcionViewSet, basename='adopcion')
router.register(r'chat-mensajes', ChatMessageViewSet, basename='chatmessage')
router.register(r'calificaciones', CalificacionViewSet, basename='calificacion')
router.register(r'notificaciones', NotificacionViewSet, basename='notificacion')

urlpatterns = router.urls
