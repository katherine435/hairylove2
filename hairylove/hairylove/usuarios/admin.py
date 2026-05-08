from django.contrib import admin
from .models import Usuario, Propietario, Criador, PasswordResetToken

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('idUsuario', 'nombre', 'apellido', 'correo', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('correo', 'nombre', 'apellido')
    readonly_fields = ('idUsuario',)

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('idPropietario', 'user', 'Cantidad_Mascotas')
    search_fields = ('user__correo',)

@admin.register(Criador)
class CriadorAdmin(admin.ModelAdmin):
    list_display = ('idCriador', 'user', 'Tipo_Criador')
    search_fields = ('user__correo',)

@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'expires_at', 'used', 'is_valid')
    list_filter = ('used', 'created_at')
    search_fields = ('user__correo', 'token')
    readonly_fields = ('token', 'created_at', 'used_at')

