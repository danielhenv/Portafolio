from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Evento


class EventoListaView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'eventos/lista_eventos.html'
    context_object_name = 'eventos'

    def get_queryset(self):
        qs = Evento.objects.all()
        user = self.request.user

        # Admin ve todos
        if user.is_superuser:
            return qs

        # asistentes / organizadores:
        #   - ven eventos públicos
        #   - eventos privados donde son organizador
        #   - eventos privados donde están en la lista de asistentes
        return qs.filter(
            Q(es_privado=False) |
            Q(organizador=user) |
            Q(asistentes=user)
        ).distinct()


class EventoDetalleView(LoginRequiredMixin, DetailView):
    model = Evento
    template_name = 'eventos/detalle_evento.html'
    context_object_name = 'evento'

    def dispatch(self, request, *args, **kwargs):
        evento = self.get_object()
        user = request.user

        # evento público → lo puede ver cualquier usuario logueado
        if not evento.es_privado:
            return super().dispatch(request, *args, **kwargs)

        # evento privado → solo admin, organizador o asistentes
        if (
            user.is_superuser
            or user == evento.organizador
            or user in evento.asistentes.all()
        ):
            return super().dispatch(request, *args, **kwargs)

        messages.error(request, 'No tienes permisos para ver este evento.')
        return redirect('eventos:acceso_denegado')


class EventoCrearView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Evento
    fields = ['titulo', 'descripcion', 'fecha', 'lugar', 'tipo', 'es_privado', 'asistentes']
    template_name = 'eventos/form_evento.html'
    permission_required = 'eventos.add_evento'
    # 👇 ADONDE REDIRIGE DESPUÉS DE CREAR
    success_url = reverse_lazy('eventos:lista_eventos')

    def get_form(self, form_class=None):
        """
        Ajustamos el campo fecha para usar <input type="datetime-local">
        y evitar el error "Enter a valid date/time".
        """
        form = super().get_form(form_class)
        # Si fecha es DateTimeField en el modelo:
        form.fields['fecha'].widget = forms.DateTimeInput(
            attrs={'type': 'datetime-local'}
        )
        # Formato que envía el navegador con datetime-local: 2025-11-30T14:30
        form.fields['fecha'].input_formats = ['%Y-%m-%dT%H:%M']
        return form

    def form_valid(self, form):
        # El organizador es siempre el usuario conectado
        form.instance.organizador = self.request.user
        messages.success(self.request, 'Evento creado correctamente.')
        return super().form_valid(form)


class EventoEditarView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Evento
    fields = ['titulo', 'descripcion', 'fecha', 'lugar', 'tipo', 'es_privado', 'asistentes']
    template_name = 'eventos/form_evento.html'
    permission_required = 'eventos.change_evento'
    # 👇 ADONDE REDIRIGE DESPUÉS DE EDITAR
    success_url = reverse_lazy('eventos:lista_eventos')

    def get_form(self, form_class=None):
        """
        Mismo widget que en la creación para que no dé error de fecha/hora.
        """
        form = super().get_form(form_class)
        form.fields['fecha'].widget = forms.DateTimeInput(
            attrs={'type': 'datetime-local'}
        )
        form.fields['fecha'].input_formats = ['%Y-%m-%dT%H:%M']
        return form

    def has_permission(self):
        """
        Solo admin o el organizador del evento pueden editarlo.
        Además, necesitan el permiso change_evento.
        """
        base = super().has_permission()
        if not base:
            return False

        evento = self.get_object()
        user = self.request.user
        return user.is_superuser or user == evento.organizador


class EventoEliminarView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Evento
    template_name = 'eventos/confirmar_eliminar.html'
    # 👇 ADONDE REDIRIGE DESPUÉS DE ELIMINAR
    success_url = reverse_lazy('eventos:lista_eventos')
    permission_required = 'eventos.delete_evento'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Evento eliminado correctamente.')
        return super().delete(request, *args, **kwargs)


def acceso_denegado(request):
    """
    Vista simple para cuando el usuario intenta entrar a algo sin permisos.
    """
    return render(request, 'eventos/acceso_denegado.html')


@login_required
def logout_view(request):
    """
    Cierra la sesión del usuario y lo redirige a la página de login.
    """
    logout(request)
    return redirect('login')