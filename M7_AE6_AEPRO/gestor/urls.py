from django.urls import path
from gestor import views

urlpatterns = [
    path('', views.main_view, name='home'),
    path('eventos/', views.lista_eventos, name='eventos_list'),
    path('eventos/<int:id>/', views.ver_evento, name='eventos_detail'),
    path('eventos/nuevo/', views.crear_evento, name='eventos_create'),
    path('eventos/editar/<int:id>/', views.editar_evento, name='eventos_update'),
    path('eventos/eliminar/<int:id>/', views.eliminar_evento, name='eventos_delete'),
    path('voluntarios/', views.lista_voluntarios, name='voluntarios_list'),
    path('voluntarios/<int:id>/', views.ver_voluntario, name='voluntarios_detail'),
    path('voluntarios/nuevo/', views.crear_voluntario, name='voluntarios_create'),
    path('voluntarios/editar/<int:id>/', views.editar_voluntario, name='voluntarios_update'),
    path('voluntarios/eliminar/<int:id>/', views.eliminar_voluntario, name='voluntarios_delete'),
]
