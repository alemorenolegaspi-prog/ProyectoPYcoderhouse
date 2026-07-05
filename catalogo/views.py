from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # <-- IMPORTANTE PARA LA SEGURIDAD
from .models import Fonograma  # (Asegurate de que coincida con el nombre de tu modelo de discos)
from .forms import DiscoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    """Vista de la página de inicio que lista y filtra los fonogramas."""
    # 1. Traemos todos los discos de la base de datos
    discos = Fonograma.objects.all()
    
    # 2. Capturamos lo que el usuario escribió en la barra de búsqueda (si escribió algo)
    buscar = request.GET.get('buscar')
    
    if buscar:
        # Filtramos si el texto coincide con el título o con el nombre del artista
        discos = discos.filter(titulo__icontains=buscar) | discos.filter(artista__icontains=buscar)
        
    return render(request, 'catalogo/home.html', {'discos': discos, 'buscar': buscar})

def detalle_disco(request, pk):
    """Vista para ver la información detallada de un solo disco."""
    disco = get_object_or_404(Fonograma, pk=pk)
    return render(request, 'catalogo/detalle_disco.html', {'disco': disco})

@login_required  # <-- BLOQUEA EL ACCESO A USUARIOS ANÓNIMOS
def crear_disco(request):
    """Vista con el formulario para registrar un nuevo fonograma."""
    if request.method == 'POST':
        # Pasamos los datos del texto (POST) y los archivos/imágenes (FILES)
        form = DiscoForm(request.POST, request.FILES)
        if form.is_valid():
            # Creamos el objeto en memoria sin impactar la BD todavía
            disco = form.save(commit=False)
            # Le asignamos de forma real el usuario que está logueado en la sesión
            disco.autor = request.user  
            # Guardamos definitivamente en la base de datos
            disco.save()
            # Redirigimos al catálogo principal
            return redirect('home')
    else:
        form = DiscoForm()
        
    return render(request, 'catalogo/crear_disco.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Lo logueamos automáticamente después de registrarse
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'catalogo/registro.html', {'form': form})

@login_required
def editar_disco(request, pk):
    """Vista para editar un fonograma existente."""
    disco = get_object_or_404(Fonograma, pk=pk)
    
    if request.method == 'POST':
        # Pasamos los datos nuevos, los archivos y le decimos qué disco estamos editando (instance=disco)
        form = DiscoForm(request.POST, request.FILES, instance=disco)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # Si entra por primera vez, carga el formulario con los datos actuales del disco
        form = DiscoForm(instance=disco)
        
    return render(request, 'catalogo/crear_disco.html', {'form': form, 'editando': True})