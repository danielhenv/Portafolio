Sistema de Reservas de Mudanzas – Aplicación Web en Django

Este proyecto consiste en una aplicación web desarrollada con el framework Django, cuyo propósito es administrar reservas de servicios de mudanza. Incluye gestión de clientes, registro de reservas, autenticación de usuarios, uso del panel de administración y una interfaz web personalizada para el acceso y visualización de la información.

Tecnologías utilizadas

Python 3

Django 5

HTML5 y CSS3

Django Templates

Django ORM

Sistema de autenticación de Django

Base de datos SQLite (configurable a MySQL u otros motores)

Funcionalidades principales
Gestión de reservas

Registro de reservas a través de un formulario basado en modelos.

Visualización del listado de reservas existentes.

Asociación directa entre clientes y reservas mediante clave foránea.

Autenticación y control de acceso

Inicio y cierre de sesión utilizando el sistema de autenticación integrado de Django.

Restricción de acceso a las vistas principales mediante decoradores de autorización.

Redirección automática según el estado de autenticación del usuario.

Panel de administración

Administración de clientes, reservas y usuarios desde el módulo de administración de Django.

Incorporación de buscadores, filtros y ordenamiento para facilitar la gestión de datos.

Configuración de permisos por usuario y por grupo.

Interfaz de usuario

Pantalla de inicio de sesión personalizada.

Plantilla base para unificar el diseño de las vistas.

Archivos estáticos organizados para aplicar estilos globales.

Estructura principal del proyecto
mudanza_django/
│
├── mudanza_site/          # Configuración general del proyecto
│   ├── settings.py
│   ├── urls.py
│
├── reservas/              # Aplicación principal
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── reservas/
│           ├── lista_reservas.html
│           └── crear_reserva.html
│
├── templates/             # Plantillas generales
│   └── registration/
│       └── login.html
│
├── static/                # Archivos estáticos
│   └── css/
│       └── estilos.css
│
└── manage.py

Instalación y ejecución
1. Creación del entorno virtual
python3 -m venv venv


Activación:

Mac/Linux:

source venv/bin/activate


Windows:

venv\Scripts\activate

2. Instalación de dependencias
pip install django

3. Migración inicial de la base de datos
python manage.py migrate

4. Creación del usuario administrador
python manage.py createsuperuser

5. Ejecución del servidor de desarrollo
python manage.py runserver

6. Acceso a secciones principales
Función	URL
Inicio de sesión	http://127.0.0.1:8000/accounts/login/

Listado de reservas	http://127.0.0.1:8000/reservas/

Registro de nueva reserva	http://127.0.0.1:8000/reservas/nueva/

Panel de administración	http://127.0.0.1:8000/admin/
Modelos implementados
Cliente

Nombre

Correo electrónico

Teléfono

Reserva

Cliente asociado

Fecha de mudanza

Hora de mudanza

Dirección de origen

Dirección de destino

Tipo de servicio

Observaciones

Las reservas mantienen una relación uno-a-muchos con los clientes.

Seguridad y permisos

Las vistas relacionadas con la gestión de reservas requieren inicio de sesión.

Se utiliza el sistema de permisos estándar de Django.

El panel de administración permite gestionar usuarios, grupos y niveles de acceso.

El diseño del flujo asegura que solo usuarios autenticados puedan registrar o visualizar reservas.

Interfaz y diseño

La pantalla de inicio de sesión cuenta con una plantilla personalizada.

Se utiliza una plantilla base para las vistas internas del sistema.

Los estilos se gestionan mediante archivos estáticos almacenados en la carpeta correspondiente.

La interfaz presenta una estructura organizada y coherente con un diseño moderno.

Conclusiones

El sistema de reservas desarrollado implementa los componentes fundamentales del framework Django, incluyendo modelos, vistas, formularios, autenticación, administración y manejo de archivos estáticos. Su estructura es adecuada para aplicaciones empresariales de baja y media complejidad, y constituye una base sólida para futuras extensiones, tales como edición y eliminación de reservas, integración con otros motores de base de datos o ampliación de funcionalidades de cliente.