from django.urls import path
from . import views

app_name = 'recetas'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recetas/', views.RecetaListView.as_view(), name='lista_recetas'),
    path('recetas/<int:pk>/', views.RecetaDetailView.as_view(), name='detalle_receta'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('contacto/enviado/', views.contacto_ok_view, name='contacto_ok'),
    path('recetas/nueva/', views.RecetaCreateView.as_view(), name='crear_receta'),
]
