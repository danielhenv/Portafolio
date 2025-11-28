from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.lista_reservas, name='lista_reservas'),
    path('nueva/', views.crear_reserva, name='crear_reserva'),
]
