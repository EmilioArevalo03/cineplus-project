from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class Pelicula(models.Model):
    GENEROS = [
        ('ACC', 'Acción'),
        ('COM', 'Comedia'),
        ('DRA', 'Drama'),
        ('SCI', 'Ciencia Ficción'),
        ('TER', 'Terror'),
        ('ROM', 'Romance'),
    ]
    
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    año = models.IntegerField()
    genero = models.CharField(max_length=3, choices=GENEROS)
    duracion = models.IntegerField(help_text="Duración en minutos")
    sinopsis = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.titulo} ({self.año})"