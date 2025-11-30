📦 Gestión de Productos – Aplicación Web en Django

Aplicación web desarrollada con Django 5, conectada a MySQL, que permite gestionar productos, categorías, etiquetas y detalles a través de operaciones CRUD.
Incluye autenticación de usuarios, seguridad CSRF, consultas avanzadas con el ORM y uso del panel administrativo de Django.
-----------------------------------------------------------------------------------
🚀 Funcionalidades principales

🟢 CRUD completo de productos

Crear, listar, editar y eliminar productos

Selección de categoría (relación Muchos a Uno)

Selección múltiple de etiquetas (relación Muchos a Muchos)

Datos adicionales del producto como dimensiones y peso (relación Uno a Uno)

🟢 Gestión de Categorías y Etiquetas

CRUD completo para ambas entidades

🟢 Consultas ORM avanzadas

Filtrar, excluir, agregar, anotar

Obtener datos usando SQL puro con raw()

Página especial en /productos/consultas/

🟢 Autenticación y seguridad

Login y Logout con django.contrib.auth

Formularios protegidos con CSRF

Menú dinámico según usuario autenticado

Sesiones activas (contador de visitas en el index)

🟢 Panel administrativo

Gestión rápida desde /admin/

🟢 Diseño moderno con CSS propio

Templates mejorados y responsivos
-----------------------------------------------------------------------------------
📁 Requisitos

Python 3.12 o superior

MySQL 8 o superior

pip
-----------------------------------------------------------------------------------
Entorno virtual recomendado

🛠 1. Clonar el repositorio
git clone https://github.com/tu_usuario/gestion_productos.git
cd gestion_productos
-----------------------------------------------------------------------------------
🛠 2. Crear y activar entorno virtual
En macOS / Linux:
python3 -m venv venv
source venv/bin/activate

En Windows (cmd):
python -m venv venv
venv\Scripts\activate
-----------------------------------------------------------------------------------
🛠 3. Instalar dependencias
pip install -r requirements.txt
-----------------------------------------------------------------------------------
🛠 4. Configurar la base de datos MySQL

En MySQL:

CREATE DATABASE gestion_productos_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER 'gestion_user'@'localhost' IDENTIFIED BY 'MiPassword123';

GRANT ALL PRIVILEGES ON gestion_productos_db.* TO 'gestion_user'@'localhost';

FLUSH PRIVILEGES;
-----------------------------------------------------------------------------------
🛠 5. Configurar Django para conectar a MySQL

En el archivo:

config/settings.py


La sección DATABASES debe verse así:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestion_productos_db',
        'USER': 'gestion_user',
        'PASSWORD': 'MiPassword123',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
-----------------------------------------------------------------------------------
🛠 6. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate
-----------------------------------------------------------------------------------
🛠 7. Crear superusuario (para el admin)
python manage.py createsuperuser
-----------------------------------------------------------------------------------
🛠 8. Ejecutar el servidor
python manage.py runserver


La aplicación estará disponible en:

➡ http://127.0.0.1:8000/
-----------------------------------------------------------------------------------
📚 Rutas principales del sistema
Página de inicio

/

Productos

/productos/ (lista)

/productos/crear/

/productos/<id>/

/productos/<id>/editar/

/productos/<id>/eliminar/

/productos/consultas/ (consultas ORM y SQL)

Categorías

/categorias/

/categorias/crear/

/categorias/<id>/editar/

/categorias/<id>/eliminar/

Etiquetas

/etiquetas/

/etiquetas/crear/

/etiquetas/<id>/editar/

/etiquetas/<id>/eliminar/

Autenticación

/accounts/login/

/accounts/logout/

Admin

/admin/

-----------------------------------------------------------------------------------