from django.shortcuts import render
from .models import Reserva

def lista_reservas(request):
    reservas = Reserva.objects.select_related('cliente').all().order_by('fecha_mudanza', 'hora_mudanza')
    return render(request, 'reservas/lista_reservas.html', {'reservas': reservas})
