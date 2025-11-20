from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    list_display = ['username', 'email', 'fecha_nacimiento', 'es_critico', 'is_staff']
    list_filter = ['es_critico', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('fecha_nacimiento', 'es_critico')}),
    )