from django import forms
from .models import Voluntario, Evento
from datetime import date

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nombre', 'email' , 'telefono']
        labels = {
            'nombre': 'Nombre del voluntario',
            'email': 'Email del voluntario',
            'telefono': 'Telefono del voluntario',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su email'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su telefono'}),
        }
        
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento 
        fields = ['titulo', 'descripcion', 'fecha']
        labels = {
            'titulo': 'Titulo del evento',
            'descripcion': 'Descripcion del evento',
            'fecha': 'Fecha del evento',    
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título del evento'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha < date.today():
            raise forms.ValidationError("La fecha del evento no puede ser en el pasado.")
        return fecha