from django.urls import path
from django.contrib.auth import views as auth_views  # <-- SE SUMA ESTA IMPORTACIÓN
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('disco/<int:pk>/', views.detalle_disco, name='detalle_disco'),
    path('nuevo/', views.crear_disco, name='crear_disco'),
    path('registro/', views.registro, name='registro'),
    
    # NUEVA RUTA: Pantalla de Login propia
    path('login/', auth_views.LoginView.as_view(template_name='catalogo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('editar/<int:pk>/', views.editar_disco, name='editar_disco'),
]