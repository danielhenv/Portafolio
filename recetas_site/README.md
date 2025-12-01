# 🍽️ App de Recetas – Proyecto Django

Este proyecto es una aplicación web desarrollada con **Django**, creada como ejercicio grupal para aprender el patrón **MTV**, navegación, rutas, vistas genéricas, formularios, manejo de archivos estáticos y diseño responsivo con **Bootstrap**.

La App de Recetas permite:
- Ver una lista de recetas.
- Ver detalles de cada receta.
- Crear nuevas recetas mediante un formulario.
- Usar un formulario de contacto con validación.
- Navegar mediante un navbar responsivo.
- Mantener una estética limpia usando Bootstrap y CSS personalizado.

---

## 🚀 Tecnologías utilizadas

- Python 3  
- Django 5  
- HTML5  
- CSS3  
- Bootstrap 5  
- SQLite  
- Templates con herencia  
- Manejo de media y staticfiles  
- Vistas genéricas: `ListView`, `DetailView`, `CreateView`

---

## 📂 Estructura del proyecto

```
recetas_site/
│
├── recetas/
│   ├── migrations/
│   ├── static/
│   │   └── recetas/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── img/
│   ├── templates/
│   │   └── recetas/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── recetas_list.html
│   │       ├── receta_detail.html
│   │       ├── receta_form.html
│   │       └── contacto.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── recetas_site/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🔧 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/recetas_site.git
cd recetas_site
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
source venv/bin/activate       # macOS / Linux
# venv\Scripts\activate        # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no existe `requirements.txt`, generarlo con:
```bash
pip freeze > requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

### 7. Abrir la aplicación

```
http://127.0.0.1:8000/
```
User:dhenriquez
Pass:123456
---

## 🧱 Funcionalidades principales

### 🏠 Página de inicio
- Jumbotron con presentación del sitio.
- Lista de últimas recetas en tarjetas.

### 📚 Listado de recetas
- Muestra todas las recetas creadas.
- Tarjetas con nombre, descripción e imagen.

### 🔍 Detalle de receta
- Ingredientes
- Instrucciones
- Imagen de referencia

### ➕ Crear nueva receta
- Formulario completo usando `ModelForm`.
- Permite subir imagen.
- Validación y redirección.

### ✉️ Página de contacto
- Formulario funcional con validación.
- Mensaje de éxito.

### 📱 Diseño responsivo
- Bootstrap 5 para móviles, tablets y desktop.

---

## 🛣️ Rutas principales

| Ruta | Descripción |
|------|-------------|
| `/` | Inicio |
| `/recetas/` | Lista de recetas |
| `/recetas/<id>/` | Detalle de receta |
| `/recetas/nueva/` | Crear receta |
| `/contacto/` | Formulario de contacto |
| `/contacto/enviado/` | Confirmación |

---

## 🛠️ Mejoras futuras

- Editar y eliminar recetas  
- Buscador  
- Categorías o etiquetas  
- Autenticación de usuarios  
- Paginación en la lista  

---

## 👥 Trabajo grupal

Este proyecto fue desarrollado aplicando:

- Colaboración con Git y GitHub  
- División de tareas  
- Buenas prácticas en Django  
- Diseño responsive y accesible  

---

## 📄 Licencia

Proyecto de uso educativo. Libre para reutilización con fines académicos.
