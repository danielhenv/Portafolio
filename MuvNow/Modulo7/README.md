# 📦 Sistema de Reservas de Mudanzas — Proyecto Django

Este proyecto implementa un **sistema de gestión de reservas de mudanzas** usando el framework **Django**, con integración completa a base de datos mediante su ORM, modelos independientes y relacionados, operaciones CRUD y el uso de aplicaciones preinstaladas como `admin`, `auth`, `sessions` y `staticfiles`.

---

# 🚀 1. Integración de Django con Bases de Datos

## ✅ ORM: la base de la integración  
Django utiliza un **ORM (Object-Relational Mapping)** que permite trabajar con tablas como si fueran **clases y objetos**, sin escribir SQL.

```python
producto = Producto.objects.create(nombre="Caja", precio=10)
productos = Producto.objects.filter(precio__gte=20)
```

Django convierte estas operaciones en SQL automáticamente.

---

## ✅ Compatibilidad con múltiples motores

| Motor           | Soportado | Requisitos                 |
|-----------------|-----------|----------------------------|
| SQLite          | ✔         | Por defecto                |
| PostgreSQL      | ✔         | `psycopg2`                 |
| MySQL/MariaDB   | ✔         | `pymysql` o `mysqlclient`  |
| Oracle          | ✔         | Cliente oficial Oracle     |

Puedes cambiar de motor editando solo `settings.py`, **sin modificar el código del proyecto**.

---

## 📌 Ejemplos de configuración en `settings.py`

### **SQLite (por defecto)**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### **PostgreSQL**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mi_base',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### **MySQL**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mi_base',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 🔌 Manejo automático de conexiones

Django administra las conexiones de forma transparente:

- Abre conexiones cuando se necesitan  
- Reutiliza conexiones (connection pooling)  
- Cierra conexiones inactivas  
- Permite ejecutar SQL manual si es necesario  

```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM reservas_reserva")
    rows = cursor.fetchall()
```

---

# 🧱 2. Modelo *Producto* como entidad independiente

En la app **reservas**, se implementó el modelo **Producto** como una entidad **simple**, sin relaciones.  
Incluye campos como:

- `nombre`  
- `precio`  
- `stock`  

Se crearon sus tablas usando:

```bash
python manage.py makemigrations reservas
python manage.py migrate
```

A partir del modelo se implementaron **operaciones CRUD** completas.

---

# 🔄 4. Migraciones en Django

Cada vez que se modificó un modelo (como `Producto` y `Reserva`), se aplicaron migraciones:

```bash
python manage.py makemigrations reservas
python manage.py migrate
```

Las migraciones generan archivos que Django convierte en SQL para actualizar la base de datos.

---

# 🔍 5. Recuperación de información con el ORM

Se usaron métodos como `filter()`, `exclude()`, `get()`, `annotate()` y consultas SQL si fue necesario.

Ejemplo: reservas de un cliente en un rango de fechas:

```python
Reserva.objects.filter(
    cliente=cliente,
    fecha_mudanza__range=(inicio, fin)
)
```

Ejemplo con `annotate`:

```python
from django.db.models import Count
Cliente.objects.annotate(
    total_reservas=Count('reserva')
)
```

---

# ⚙️ 7. Uso de aplicaciones preinstaladas de Django

El proyecto usa varias apps del núcleo de Django:

### ✔ `django.contrib.admin`
- Gestión de Cliente, Reserva y Producto  
- Columnas personalizadas  
- Filtros y buscadores  
- Funcionalidad similar a un sistema real

### ✔ `django.contrib.auth`
- Autenticación de usuarios  
- Protege vistas con `@login_required`  
- Rutas `/accounts/login/` y `/accounts/logout/`

### ✔ `django.contrib.sessions`
- Manejo automático de sesiones

### ✔ `django.contrib.messages`
- Mensajes de confirmación y error

### ✔ `django.contrib.staticfiles`
- Manejo de archivos estáticos (ej: `estilos.css`)

---

# 🏗️ Sistema de Reservas de Mudanzas — Configuración del Proyecto

## 📥 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd mudanza_django
```

---

## 🧰 2. Crear entorno virtual

```bash
python -m venv venv
```

Activarlo:

**Linux/MacOS**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

---

## 📦 3. Instalar dependencias

```bash
pip install django
```

MySQL:
```bash
pip install pymysql
```

PostgreSQL:
```bash
pip install psycopg2-binary
```

python manage.py collectstatic
---

# 🗄️ 4. Configuración de base de datos

Se realiza en:

```
mudanza_site/settings.py
```

Ejemplos arriba 👆

---

# 🧱 5. Migraciones

Crear migraciones:

```bash
python manage.py makemigrations
```

Aplicarlas:

```bash
python manage.py migrate
```

---

# ▶️ 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Acceder:

- Login → http://127.0.0.1:8000/accounts/login/  
- Reservas → http://127.0.0.1:8000/reservas/  
- Admin → http://127.0.0.1:8000/admin/ *(admin/admin)*

---

# 🧩 7. Modelos y relaciones

### ✔ Modelo independiente
`Producto` → sin relaciones directas

### ✔ Modelos relacionados

- **Cliente — Reserva** → relación *1 a muchos*
- **Reserva — Producto** → *muchos a muchos* si se extiende

Implementado con:

- `ForeignKey`
- `ManyToManyField`
- `OneToOneField` (si fuera necesario)

---

# 📝 8. CRUD implementado

CRUD completo para:

✔ Clientes  
✔ Reservas  
✔ Productos  

Cada operación usa ORM + formularios + templates.

---

# 🔎 9. Consultas avanzadas

Ejemplos:

```python
reservas = Reserva.objects.filter(cliente__nombre="Juan")
productos_caros = Producto.objects.filter(precio__gt=50000)
```

---

# 🧩 10. SQL personalizado

```python
Reserva.objects.raw("SELECT * FROM reservas_reserva WHERE precio > 10000")
```

---
