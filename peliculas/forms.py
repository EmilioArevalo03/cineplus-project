from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'director', 'año', 'genero', 'duracion', 'sinopsis']
        widgets = {
            'sinopsis': forms.Textarea(attrs={'rows': 4}),
            'año': forms.NumberInput(attrs={'min': 1900, 'max': 2030}),
        }