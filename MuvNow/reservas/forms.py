from django import forms
from .models import Reserva, Cliente
from .models import Producto

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'cliente',
            'producto',
            'fecha_mudanza',
            'hora_mudanza',
            'direccion_origen',
            'direccion_destino',
            'tipo_servicio',
            'notas',
        ]
        widgets = {
            'fecha_mudanza': forms.DateInput(attrs={'type': 'date'}),
            'hora_mudanza': forms.TimeInput(attrs={'type': 'time'}),
            'notas': forms.Textarea(attrs={'rows': 3}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'cantidad']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']
