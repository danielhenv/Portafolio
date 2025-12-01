from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.lista_reservas, name='lista_reservas'),
    path('nueva/', views.crear_reserva, name='crear_reserva'),

    # CRUD de productos
    path('productos/', views.ProductoListaView.as_view(), name='producto_lista'),
    path('productos/nuevo/', views.ProductoCrearView.as_view(), name='producto_crear'),
    path('productos/<int:pk>/editar/', views.ProductoEditarView.as_view(), name='producto_editar'),
    path('productos/<int:pk>/eliminar/', views.ProductoEliminarView.as_view(), name='producto_eliminar'),
]
