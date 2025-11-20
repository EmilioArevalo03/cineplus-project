from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pelicula
from .forms import PeliculaForm

@login_required
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/lista_peliculas.html', {'peliculas': peliculas})

@login_required
def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            pelicula = form.save(commit=False)
            pelicula.usuario = request.user
            pelicula.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/form_pelicula.html', {'form': form, 'titulo': 'Crear Película'})

@login_required
def editar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm(instance=pelicula)
    
    return render(request, 'peliculas/form_pelicula.html', {'form': form, 'titulo': 'Editar Película'})

@login_required
def eliminar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    
    if request.method == 'POST':
        pelicula.delete()
        return redirect('lista_peliculas')
    
    return render(request, 'peliculas/confirmar_eliminar.html', {'pelicula': pelicula})

def detalle_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'peliculas/detalle_pelicula.html', {'pelicula': pelicula})