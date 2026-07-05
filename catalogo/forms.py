from django import forms
from .models import Fonograma

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Fonograma
        # Sacamos 'autor' de la lista para manejarlo de forma segura en la vista
        fields = ['titulo', 'artista', 'ano_edicion', 'sello_discografico', 'formato', 'resena', 'portada']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'artista': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_edicion': forms.NumberInput(attrs={'class': 'form-control'}),
            'sello_discografico': forms.TextInput(attrs={'class': 'form-control'}),
            'formato': forms.Select(attrs={'class': 'form-control'}), # <-- ¡Lo cambié a Select para que use tus solapas de Vinilo, CD, etc.!
            'resena': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'portada': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        