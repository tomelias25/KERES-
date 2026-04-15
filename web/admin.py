from django.contrib import admin
from .models import Cultivo, Suelo


from django.contrib import admin
from .models import Cultivo, Suelo


@admin.register(Suelo)
class SueloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'ph', 'drenaje')
    list_filter = ('tipo', 'ph')
    search_fields = ('nombre',)
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'descripcion', 'imagen')
        }),
        ('Características', {
            'fields': ('tipo', 'ph', 'drenaje')
        }),
        ('Cultivos', {
            'fields': ('cultivos_recomendados',)
        }),
    )


@admin.register(Cultivo)
class CultivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'suelo', 'region', 'clima', 'temporada', 'rendimiento_ha')
    list_filter = ('suelo', 'region', 'clima', 'temporada')
    search_fields = ('nombre',)
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'descripcion', 'imagen', 'suelo')
        }),
        ('Ubicación', {
            'fields': ('region', 'altura_minima', 'altura_maxima')
        }),
        ('Condiciones de cultivo', {
            'fields': ('clima', 'temporada', 'rendimiento_ha')
        }),
    )