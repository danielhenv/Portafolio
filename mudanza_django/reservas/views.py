from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm
from .models import Reserva


@login_required
def lista_reservas(request):
    """
    Vista que muestra todas las reservas registradas.
    """
    reservas = Reserva.objects.select_related('cliente').all().order_by('fecha_mudanza', 'hora_mudanza')
    context = {
        'reservas': reservas
    }
    return render(request, 'reservas/lista_reservas.html', context)


@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.creado_por = request.user
            reserva.save()
            return redirect('reservas:lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form})


