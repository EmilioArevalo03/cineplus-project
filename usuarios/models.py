from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    fecha_nacimiento = models.DateField(null=True, blank=True)
    es_critico = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username