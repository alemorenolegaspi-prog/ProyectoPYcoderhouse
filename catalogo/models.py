from django.db import models
from django.contrib.auth.models import User

class Fonograma(models.Model):
    # Campos técnicos del disco
    titulo = models.CharField(max_length=200, verbose_name="Título del Álbum")
    artista = models.CharField(max_length=200, verbose_name="Artista / Banda")
    ano_edicion = models.IntegerField(verbose_name="Año de Edición")
    sello_discografico = models.CharField(max_length=100, verbose_name="Sello Discográfico")
    
    # Opciones de formato
    FORMATO_CHOICES = [
        ('VINILO', 'Vinilo'),
        ('CD', 'CD'),
        ('CASSETTE', 'Cassette'),
        ('DIGITAL', 'Digital'),
    ]
    formato = models.CharField(max_length=20, choices=FORMATO_CHOICES, default='CD')
    
    # Contenido tipo Blog
    resena = models.TextField(blank=True, verbose_name="Reseña o Comentarios")
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True, verbose_name="Imagen de Portada")
    
    # Relación con el usuario que lo carga
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cargado por")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.artista} - {self.titulo}"