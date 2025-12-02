from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RecetaForm
from .models import Receta
from .forms import ContactoForm

from django.http import Http404

class HomeView(ListView):
    model = Receta
    template_name = 'home.html'
    context_object_name = 'recetas'

class RecetaListView(ListView):
    model = Receta
    template_name = 'recetas_list.html'
    context_object_name = 'recetas'

    def get_queryset(self):
        return Receta.objects.all().order_by('-id')

class RecetaDetailView(DetailView):
    model = Receta
    template_name = 'receta_detail.html'
    context_object_name = 'receta'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            
            raise

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            return redirect('recetas:contacto_ok')
        else:
            messages.warning(request, "Completa todos los campos.")
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

def contacto_ok_view(request):
    return render(request, 'contacto_ok.html')



class HomeView(ListView):
    model = Receta
    template_name = 'home.html'
    context_object_name = 'recetas'

    def get_queryset(self):
        return Receta.objects.all().order_by('-id')[:6]
    

def mi_error_404(request, exception):
    return render(request, '404.html', status=404)



def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Aqui se podria enviar un email o guardar en BD
            messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
            return redirect('recetas:contacto_ok')
        else:
            messages.warning(request, 'Por favor, completa correctamente todos los campos.')
    else:
        form = ContactoForm()
    return render(request, 'recetas/contacto.html', {'form': form})

def contacto_ok_view(request):
    return render(request, 'recetas/contacto_ok.html')


class RecetaCreateView(CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'recetas/receta_form.html'
    success_url = reverse_lazy('recetas:lista_recetas')
