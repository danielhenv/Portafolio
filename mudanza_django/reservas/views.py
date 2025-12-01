from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm
from .models import Reserva
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Producto


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



class ProductoListaView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'reservas/producto_lista.html'
    context_object_name = 'productos'


class ProductoCrearView(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['nombre', 'precio', 'cantidad']
    template_name = 'reservas/producto_form.html'
    success_url = reverse_lazy('reservas:producto_lista')


class ProductoEditarView(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'cantidad']
    template_name = 'reservas/producto_form.html'
    success_url = reverse_lazy('reservas:producto_lista')


class ProductoEliminarView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'reservas/producto_confirmar_eliminar.html'
    success_url = reverse_lazy('reservas:producto_lista')


