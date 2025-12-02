from django import forms

from .models import Receta

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    


class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'ingredientes', 'instrucciones', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'instrucciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
