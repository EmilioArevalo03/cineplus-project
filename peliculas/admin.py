from django.contrib import admin
from .models import Pelicula

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'director', 'año', 'genero', 'usuario']
    list_filter = ['genero', 'año']
    search_fields = ['titulo', 'director']