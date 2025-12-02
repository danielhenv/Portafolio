from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.lista_reservas, name='lista_reservas'),
    path('nueva/', views.crear_reserva, name='crear_reserva'),
    path('<int:pk>/editar/', views.editar_reserva, name='editar_reserva'),
    path('<int:pk>/eliminar/', views.eliminar_reserva, name='eliminar_reserva'),

    # CRUD de productos
    path('productos/', views.producto_lista, name='producto_lista'),
    path('productos/nuevo/', views.producto_crear, name='producto_crear'),
    path('productos/<int:pk>/editar/', views.producto_editar, name='producto_editar'),
    path('productos/<int:pk>/eliminar/', views.producto_eliminar, name='producto_eliminar'),

    #CLIENTES
    path('clientes/', views.ClienteListaView.as_view(), name='cliente_lista'),
    path('clientes/nuevo/', views.ClienteCrearView.as_view(), name='cliente_crear'),
    path('clientes/<int:pk>/editar/', views.ClienteEditarView.as_view(), name='cliente_editar'),
    path('clientes/<int:pk>/eliminar/', views.ClienteEliminarView.as_view(), name='cliente_eliminar'),
]
