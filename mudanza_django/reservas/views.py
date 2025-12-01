from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm
from .models import Reserva
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Producto
from django.contrib import messages
from .forms import ProductoForm


@login_required
def lista_reservas(request):
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
            # si tienes un campo creado_por en Reserva, descomenta:
            # reserva.creado_por = request.user
            reserva.save()
            messages.success(request, 'Reserva creada correctamente.')
            return redirect('reservas:lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form})


@login_required
def editar_reserva(request, pk):
    """
    Editar una reserva existente.
    """
    reserva = get_object_or_404(Reserva, pk=pk)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva actualizada correctamente.')
            return redirect('reservas:lista_reservas')
    else:
        form = ReservaForm(instance=reserva)

    context = {
        'form': form,
        'reserva': reserva,
    }
    return render(request, 'reservas/editar_reserva.html', context)


@login_required
def eliminar_reserva(request, pk):
    """
    Mostrar confirmación y eliminar una reserva.
    """
    reserva = get_object_or_404(Reserva, pk=pk)

    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'Reserva eliminada correctamente.')
        return redirect('reservas:lista_reservas')

    # GET → mostrar pantalla de confirmación
    context = {
        'reserva': reserva,
    }
    return render(request, 'reservas/confirmar_eliminar_reserva.html', context)



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


# ---------- CRUD de Producto ----------

@login_required
def producto_lista(request):
    productos = Producto.objects.all()
    return render(request, 'reservas/producto_lista.html', {'productos': productos})


@login_required
def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('reservas:producto_lista')
    else:
        form = ProductoForm()
    return render(request, 'reservas/producto_form.html', {'form': form, 'titulo': 'Nuevo producto'})


@login_required
def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('reservas:producto_lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'reservas/producto_form.html', {'form': form, 'titulo': 'Editar producto'})


@login_required
def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('reservas:producto_lista')
    return render(request, 'reservas/producto_confirmar_eliminar.html', {'producto': producto})


