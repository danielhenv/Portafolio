App Mudanza – Sistema de Reservas en Django

Este proyecto implementa un sistema web para gestionar reservas de mudanzas.
Fue desarrollado utilizando Django, con autenticación, administración de usuarios, formularios validados y una interfaz moderna basada en plantillas personalizadas.

🧰 Tecnologías utilizadas

Python 3

Django 5

HTML5 / CSS3

Django Templates

Django ORM

Autenticación con Django Auth

SQLite (por defecto)

Django Admin

📦 Funcionalidades principales
✔ Gestión de reservas

Listado de reservas en tabla estilizada.

Creación de nuevas reservas mediante formulario validado.

Relación Cliente → Reserva.

✔ Autenticación de usuarios

Inicio y cierre de sesión.

Redirección automática según estado del usuario.

Rutas protegidas mediante login_required.

✔ Panel de administración

Administración completa de:

Clientes

Reservas

Usuarios y permisos

Búsquedas por nombre, email y direcciones.

Filtros por tipo de servicio y fecha.

Navegación por jerarquía temporal (date_hierarchy).

✔ Interfaz moderna

Pantalla de login con fondo degradado estilo app profesional.

Layout global con diseño oscuro.

Botones redondeados y tabla estilizada.

Formularios con inputs y validación visual limpia.

🗂 Estructura del proyecto
mudanza_django/
│
├── mudanza_site/          # Configuración general del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── reservas/              # Aplicación principal
│   ├── models.py          # Modelos Cliente y Reserva
│   ├── forms.py           # Formulario de reserva
│   ├── views.py           # Lógica de vistas
│   ├── urls.py            # Rutas principales
│   └── templates/
│       └── reservas/      # Templates de la app
│
├── templates/             # Plantillas globales
│   └── registration/
│       ├── login.html     # Pantalla de login personalizada
│       └── logged_out.html (opcional)
│
├── static/                # Archivos estáticos
│   └── css/
│       └── estilos.css
│
└── manage.py

🔧 Instalación y ejecución
1. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

2. Instalar dependencias
pip install django

3. Migrar base de datos
python manage.py migrate

4. Crear superusuario
python manage.py createsuperuser

5. Ejecutar servidor de desarrollo
python manage.py runserver

6. Acceder a las páginas principales
Sección	URL
Login	http://127.0.0.1:8000/accounts/login/

Listado de reservas	http://127.0.0.1:8000/reservas/

Crear nueva reserva	http://127.0.0.1:8000/reservas/nueva/

Panel de administración	http://127.0.0.1:8000/admin/
🧩 Modelos principales
🧑 Cliente

nombre

email

telefono

📦 Reserva

cliente (FK)

fecha_mudanza

hora_mudanza

direccion_origen

direccion_destino

tipo_servicio

notas

Relación: un Cliente puede tener varias Reservas.

🔐 Seguridad y permisos

Rutas críticas protegidas con @login_required.

Autenticación incorporada con django.contrib.auth.

Administración completa desde /admin/:

Creación de usuarios

Permisos personalizados

Grupos

Personalización del admin con:

Columnas (list_display)

Filtros (list_filter)

Buscadores (search_fields)

Navegación por fecha (date_hierarchy)

🎨 Diseño e interfaz

Pantalla de login inspirada en diseños modernos con fondo degradado.

Interfaz oscura con tarjetas, tablas y botones estilizados.

CSS propio ubicado en static/css/estilos.css.

Plantilla base base.html para mantener una estética coherente.

📘 Conclusión

Este proyecto demuestra:

Dominio del framework Django

Manejo de modelos, formularios, vistas y URLs

Autenticación, autorización y gestión de usuarios

Personalización del admin

Uso de plantillas y archivos estáticos

Diseño moderno y organización profesional del código

Es una base sólida para sistemas empresariales reales.