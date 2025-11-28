from django import forms
from .models import Reserva, Cliente

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'cliente',
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
        }
