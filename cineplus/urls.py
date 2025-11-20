from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuarios.views import logout_view  # ← IMPORTACIÓN CORRECTA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('peliculas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),  # ← Ahora está definido
]