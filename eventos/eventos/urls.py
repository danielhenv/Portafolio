from django.urls import path
from .views import (
    EventoListaView,
    EventoDetalleView,
    EventoCrearView,
    EventoEditarView,
    EventoEliminarView,
    acceso_denegado
)

app_name = 'eventos'

urlpatterns = [
    path('', EventoListaView.as_view(), name='lista_eventos'),
    path('<int:pk>/', EventoDetalleView.as_view(), name='evento_detalle'),
    path('crear/', EventoCrearView.as_view(), name='evento_crear'),
    path('<int:pk>/editar/', EventoEditarView.as_view(), name='evento_editar'),
    path('<int:pk>/eliminar/', EventoEliminarView.as_view(), name='evento_eliminar'),
    path('acceso-denegado/', acceso_denegado, name='acceso_denegado'),
]


