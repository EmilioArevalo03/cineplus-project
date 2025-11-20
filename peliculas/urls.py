from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_peliculas, name='lista_peliculas'),
    path('pelicula/nueva/', views.crear_pelicula, name='crear_pelicula'),
    path('pelicula/<int:pk>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('pelicula/<int:pk>/editar/', views.editar_pelicula, name='editar_pelicula'),
    path('pelicula/<int:pk>/eliminar/', views.eliminar_pelicula, name='eliminar_pelicula'),
]