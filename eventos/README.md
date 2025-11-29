Plataforma de Gestión de Eventos – Proyecto Django

Este proyecto corresponde a una plataforma web desarrollada con Django cuyo objetivo es gestionar eventos como conferencias, seminarios y actividades privadas.
Incluye autenticación de usuarios, manejo de permisos, roles específicos, control de acceso a eventos privados y uso de vistas basadas en clases.

1. Objetivo del proyecto

El propósito de la aplicación es permitir que diferentes tipos de usuarios interactúen con un sistema de gestión de eventos de acuerdo con sus permisos:

Administrador: tiene control total sobre todos los eventos.

Organizador: puede crear y editar eventos, exclusivamente aquellos donde figura como organizador.

Asistente: puede visualizar únicamente los eventos públicos y los eventos privados a los que está invitado.

El desarrollo integra el sistema de autenticación y autorización del modelo Auth de Django, aplicando roles, mixins, permisos y restricciones por usuario.

2. Tecnologías utilizadas

Python 3

Django 5

HTML5 / CSS3

Django Templates

SQLite (base de datos por defecto)

Django ORM

Django Auth (login, logout, permisos, sesiones)

3. Funcionalidades implementadas
3.1 Gestión de eventos

Listado de eventos con visibilidad según permisos del usuario.

Visualización del detalle del evento.

Creación, edición y eliminación de eventos (según roles).

Diferenciación de eventos públicos y privados.

Relación entre organizador y asistentes.

3.2 Autenticación

Inicio de sesión

Cierre de sesión

Rutas protegidas (LoginRequiredMixin)

Redirección después de login (LOGIN_REDIRECT_URL)

Pantalla de acceso denegado para intentos no autorizados

3.3 Roles y permisos

Uso de PermissionRequiredMixin para restringir creación, edición y eliminación.

Configuración de permisos dentro de Django Admin:

eventos.add_evento

eventos.change_evento

eventos.delete_evento

3.4 Control de acceso a eventos privados

El sistema determina si un usuario tiene o no autorización para ver un evento privado basándose en:

Si es administrador

Si es organizador de ese evento

Si figura en la lista de asistentes

Si no cumple, se le redirige a una vista de acceso denegado.

4. Estructura del proyecto
eventos/
│
├── eventos_site/
│   ├── settings.py
│   ├── urls.py
│
├── eventos/
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│       └── eventos/
│           ├── lista_eventos.html
│           ├── detalle_evento.html
│           ├── form_evento.html
│           ├── confirmar_eliminar.html
│           └── acceso_denegado.html
│
├── templates/
│   └── registration/
│       ├── login.html
│       └── logged_out.html
│
├── static/
│   └── css/
│       └── estilos.css
│
└── manage.py

5. Modelos principales
Modelo Evento

Incluye:

Título

Descripción

Fecha y hora

Lugar

Tipo de evento

Campo booleano para indicar si es privado

Organizador (ForeignKey a Usuario)

Lista de asistentes (ManyToManyField)

6. Implementación de vistas y permisos

Las vistas se implementaron utilizando Class Based Views y los mixins de autenticación/autorización:

✔ LoginRequiredMixin

Garantiza que el usuario esté autenticado antes de acceder a la vista.

✔ PermissionRequiredMixin

Aplica permisos específicos sobre la acción:

Crear eventos → eventos.add_evento

Editar eventos → eventos.change_evento

Eliminar eventos → eventos.delete_evento

✔ Validación personalizada

Para eventos privados:

El sistema valida autorización antes de permitir la visualización.

Si el usuario no cumple los requisitos, se redirige a "Acceso denegado".

7. Configuración de rutas
Rutas principales

eventos_site/urls.py incluye las rutas globales:

path('accounts/', include('django.contrib.auth.urls')),
path('eventos/', include(('eventos.urls', 'eventos'), namespace='eventos')),

Rutas de la app "eventos"
path('', EventoListaView.as_view(), name='lista_eventos'),
path('<int:pk>/', EventoDetalleView.as_view(), name='evento_detalle'),
path('crear/', EventoCrearView.as_view(), name='evento_crear'),
path('<int:pk>/editar/', EventoEditarView.as_view(), name='evento_editar'),
path('<int:pk>/eliminar/', EventoEliminarView.as_view(), name='evento_eliminar'),
path('acceso-denegado/', acceso_denegado, name='acceso_denegado'),

8. Autenticación

Django Auth se utiliza para todas las acciones de inicio/cierre de sesión:

/accounts/login/

/accounts/logout/

Redirecciones automáticas según LOGIN_REDIRECT_URL y LOGOUT_REDIRECT_URL

Además, todos los templates utilizan el contexto user proporcionado por Django para validar permisos y mostrar opciones dinámicamente.

9. Prueba del funcionamiento
✔ Rol Administrador

Puede acceder al admin /admin/

Puede crear, editar y eliminar eventos

Ve todos los eventos, incluidos privados

✔ Rol Organizador

Puede crear eventos

Puede editar solo sus propios eventos

No puede eliminar eventos (si no tiene permiso)

✔ Rol Asistente

Puede iniciar sesión

Ve eventos públicos

Ve solo eventos privados donde está invitado

✔ Evento privado

Si un usuario no autorizado intenta entrar:
→ Se le redirige a /eventos/acceso-denegado/

10. Instalación y ejecución
Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

Instalar dependencias
pip install django

Migrar
python manage.py migrate

Crear superusuario
python manage.py createsuperuser

Ejecutar servidor
python manage.py runserver

11. Conclusión

Este proyecto integra múltiples funcionalidades avanzadas de Django:

Sistema de roles utilizando permisos

Autenticación y autorización

Restricción de acceso con mixins

Control de eventos privados

Uso correcto de vistas basadas en clases

Administración completa desde Django Admin

Manejo visual de errores y mensajes

La aplicación cumple con los requerimientos de la unidad y puede ser fácilmente extendida para funciones adicionales como registro de usuarios, comentarios o filtrado avanzado de eventos.