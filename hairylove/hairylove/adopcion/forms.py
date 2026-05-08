from django import forms
from .models import Mascota, Adopcion
from django.utils import timezone
from .razas import RAZAS_POR_ESPECIE, ESPECIES


class MascotaAdopcionForm(forms.ModelForm):
    """Formulario para registrar una mascota en adopción"""
    
    # Definir choices para Especie
    ESPECIE_CHOICES = [(especie, especie) for especie in ESPECIES]
    ESPECIE_CHOICES.insert(0, ('', '---------'))
    
    # Generar todas las razas disponibles
    TODAS_LAS_RAZAS = set()
    for razas in RAZAS_POR_ESPECIE.values():
        TODAS_LAS_RAZAS.update(razas)
    TODAS_LAS_RAZAS = sorted(list(TODAS_LAS_RAZAS))
    RAZA_CHOICES = [(raza, raza) for raza in TODAS_LAS_RAZAS]
    RAZA_CHOICES.insert(0, ('', '---------'))
    
    # Campos con Select en lugar de TextInput
    Especie = forms.ChoiceField(
        choices=ESPECIE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        label='Especie'
    )
    
    # Raza como TextInput para permitir razas personalizadas
    Raza = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        label='Raza'
    )
    
    class Meta:
        model = Mascota
        fields = [
            'Nombre_Mascota', 'Fecha_Nacimiento', 'Especie', 'Raza', 'Genero', 
            'Peso', 'Color', 'Tamaño', 'Historial_Mascota', 'Tipo_Alimentación',
            'Enfermedades', 'Vivienda', 'Vacunas', 'Compatibilidad_Mascota',
            'Descripción_Física', 'Estado_Salud', 'Esterilizado', 'Socializado',
            'foto_mascota', 'Origen'
        ]
        widgets = {
            'Nombre_Mascota': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la mascota'
            }),
            'Fecha_Nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'Peso': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Peso en kg',
                'step': '0.1'
            }),
            'Color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Color o patrón de pelaje'
            }),
            'Tamaño': forms.Select(attrs={
                'class': 'form-control'
            }),
            'Historial_Mascota': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Historias, eventos destacables...'
            }),
            'Tipo_Alimentación': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Croquetas, dieta especial, etc.'
            }),
            'Enfermedades': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enfermedades previas, alergias, condiciones...'
            }),
            'Vivienda': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Casa con patio, Apartamento, etc.'
            }),
            'Vacunas': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Vacunas aplicadas y fechas...'
            }),
            'Compatibilidad_Mascota': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Cómo se lleva con otros animales, niños, etc.'
            }),
            'Descripción_Física': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción detallada de su apariencia'
            }),
            'Estado_Salud': forms.Select(attrs={'class': 'form-control'}),
            'Esterilizado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Socializado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'foto_mascota': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'Origen': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'Nombre_Mascota': 'Nombre de la Mascota',
            'Fecha_Nacimiento': 'Fecha de Nacimiento',
            'Raza': 'Raza',
            'Genero': 'Género',
            'Peso': 'Peso (kg)',
            'Especie': 'Especie',
            'Color': 'Color/Patrón',
            'Tamaño': 'Tamaño',
            'Historial_Mascota': 'Historial de la Mascota',
            'Tipo_Alimentación': 'Tipo de Alimentación',
            'Enfermedades': 'Enfermedades o Condiciones',
            'Vivienda': 'Tipo de Vivienda Recomendado',
            'Vacunas': 'Registro de Vacunas',
            'Compatibilidad_Mascota': 'Compatibilidad con Otros Animales/Niños',
            'Descripción_Física': 'Descripción Física',
            'Estado_Salud': 'Estado de Salud Actual',
            'Esterilizado': '¿Está esterilizado/castrado?',
            'Socializado': '�Está socializado?',
            'foto_mascota': 'Foto de la Mascota',
            'Origen': 'Origen de la Mascota',
        }


class AdopcionForm(forms.ModelForm):
    """Formulario para que un propietario solicite una adopción"""
    
    class Meta:
        model = Adopcion
        fields = [
            'Motivo_Adopción', 'Lugar_Vivienda', 'Info_Mascota',
            'Estado_Ingreso_Mascota'
        ]
        widgets = {
            'Motivo_Adopción': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': '¿Por qué deseas adoptar esta mascota?'
            }),
            'Lugar_Vivienda': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe tu vivienda (tipo, espacio, patio, etc.)'
            }),
            'Info_Mascota': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': '¿Tienes otras mascotas? Describe el ambiente'
            }),
            'Estado_Ingreso_Mascota': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': '¿Cómo planeas la adaptación de la mascota?'
            }),
        }
        labels = {
            'Motivo_Adopción': 'Motivo de la Adopción',
            'Lugar_Vivienda': 'Descripción de tu Vivienda',
            'Info_Mascota': 'Información sobre Mascotas Actuales',
            'Estado_Ingreso_Mascota': 'Plan de Adaptación de la Mascota',
        }


class CargaMasivaForm(forms.Form):
    """Formulario para carga masiva de mascotas desde Excel"""
    archivo_excel = forms.FileField(
        label="Selecciona el archivo Excel",
        help_text="Sube un archivo .xlsx con las mascotas. Formato esperado: columnas 'Nombre_Mascota', 'Fecha_Nacimiento', 'Raza', 'Genero', 'Peso', 'Especie', 'Color', 'Tamaño', 'Historial_Mascota', 'Tipo_Alimentación', 'Enfermedades', 'Vivienda', 'Vacunas', 'Compatibilidad_Mascota', 'Descripción_Física'."
    )


class ChatMessageForm(forms.Form):
    """Formulario para enviar mensajes de chat entre usuarios."""
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Escribe un mensaje...'
        }),
        max_length=1000,
        required=True,
        label='Mensaje'
    )


class CalificacionForm(forms.Form):
    """Formulario para calificar a un usuario después de una adopción"""
    
    PUNTUACION_CHOICES = [
        (1, '⭐ 1 - Muy Malo'),
        (2, '⭐⭐ 2 - Malo'),
        (3, '⭐⭐⭐ 3 - Regular'),
        (4, '⭐⭐⭐⭐ 4 - Bueno'),
        (5, '⭐⭐⭐⭐⭐ 5 - Excelente'),
    ]
    
    puntuacion = forms.ChoiceField(
        choices=PUNTUACION_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Puntuación',
        required=True
    )
    
    comentario = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Comparte tu experiencia (opcional)'
        }),
        label='Comentario',
        required=False,
        max_length=1000
    )
