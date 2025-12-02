# 📘 README – Portafolio de Proyectos del Curso Full Stack Python / Django

Este repositorio reúne todos los proyectos desarrollados durante mi proceso formativo, demostrando mis habilidades en **Django, bases de datos, Python, MVC/MTV, Bootstrap, frontend, control de versiones y construcción de aplicaciones funcionales**.

Cada proyecto está documentado con su **contexto, funcionalidades, aprendizajes, retos encontrados y soluciones aplicadas**.

---

## 📂 Índice de Proyectos

1. 🏠 **Mudanza Django – Sistema de reservas**  
2. 🎫 **Eventos Django – Roles, permisos y acceso privado**  
3. 🗃️ **Ejercicios ORM y SQL – Consultas avanzadas**  
4. 🍽️ **Sitio de Recetas – Django + Bootstrap + imágenes**  
5. 🧑‍🏫 **Sistema Académico – Relaciones 1:1, 1:N y N:N**  
6. 🔍 **Proyecto de Revisión Final – Correcciones y refactorización**  
7. 💼 **Portafolio Profesional – Sitio web estático**  
8. 🚀 **Portafolio Final Profesional – Proyecto para empleadores**

---

# 🏠 1. Mudanza Django – Sistema de Reservas

### ✔ Funcionalidades implementadas
- CRUD completo de **Reservas**, **Clientes** y **Productos**  
- Autenticación con Django Auth  
- Inicio/cierre de sesión con páginas personalizadas  
- Integración con Bootstrap  
- URLs organizadas por app  
- Relaciones entre modelos  

### 🚧 Principales retos
- Errores **NoReverseMatch** en URLs  
- Manejo de `staticfiles`  
- Importaciones circulares  
- Configuración de templates  

### 🛠️ Soluciones aplicadas
- Uso correcto de `app_name` y namespaces  
- Estructura profesional `/templates/reservas/`  
- Separación clara de modelos  
- Ajuste de `STATIC_URL` y carga de assets  

---

# 🎫 2. Sistema de Eventos – Roles y Permisos

### ✔ Características principales
- Gestión de eventos públicos y privados  
- Roles:
  - Administrador  
  - Organizador  
  - Asistente  
- Permisos:
  - `add_evento`  
  - `change_evento`  
  - `delete_evento`  
- Uso de mixins:
  - `LoginRequiredMixin`  
  - `PermissionRequiredMixin`  
- Acceso dinámico según el usuario  

### 🚧 Retos enfrentados
- Error: *“Enter a valid date/time”*  
- Redirecciones incorrectas en login/logout  
- Namespaces mal definidos  

### 🛠️ Soluciones
- Uso de: `DateTimeInput(type="datetime-local")`  
- Implementación de `get_success_url()`  
- Definición correcta de `app_name = "eventos"`  

---

# 🗃️ 3. Ejercicios ORM y SQL – Consultas avanzadas

### ✔ Consultas realizadas
- `filter()`, `exclude()`, `annotate()`  
- SQL crudo con `.raw()`  
- Consultas parametrizadas  
- Uso de `connection.cursor()`  
- Pruebas con índices de base de datos  

### 🚧 Retos
- Diferencia entre ORM vs SQL manual  
- Mapear resultados de `.raw()` a modelos Django  

---

# 🍽️ 4. Sitio de Recetas – Django + Bootstrap

### ✔ Funcionalidades
- Página de inicio con jumbotron  
- Lista de recetas con imágenes  
- Detalles de receta  
- Formulario de contacto  
- Template base con navbar y footer  
- Manejo de imágenes en `MEDIA_ROOT`  
- Diseño responsivo con Bootstrap  

### 🚧 Retos
- Rutas dinámicas en templates  
- Configuración de imágenes  
- Diseño responsivo  

---

# 🧑‍🏫 5. Sistema Académico – Relaciones avanzadas

### ✔ Modelos implementados
- **Profesor → Cursos** (1:N)  
- **Estudiante ↔ Curso** mediante Inscripción (N:N con modelo intermedio)  
- **Perfil ↔ Estudiante** (1:1)  

### ✔ Pruebas realizadas
- Crear profesores con cursos  
- Crear estudiantes e inscribirlos  
- Cambiar estado de inscripción  
- Borrado en cascada  

---

# 🔍 6. Proyecto de Revisión Final

### ✔ Actividades realizadas
- Revisión completa del código  
- Identificación de mejoras  
- Refactorización  
- Feedback entre compañeros  
- Corrección de errores en:  
  - CSS  
  - Rutas  
  - Validaciones  
- Documentación clara en README  

---

# 💼 7. Portafolio Profesional – Sitio Estático (HTML + CSS)

### ✔ Páginas creadas
- `index.html` – Sección principal  
- `sobre-mi.html` – Biografía extendida  
- `proyectos.html` – Proyectos con imágenes  
- `contacto.html` – Formulario simple  

### ✔ Diseño
- Moderno y responsivo  
- Navbar profesional  
- Uso de imágenes de stock  
- CSS bien estructurado  

---

# 🚀 8. Portafolio Final Profesional (Proyecto Final)

### ✔ Requisitos cumplidos
- Explicación completa del portafolio  
- Desarrollo de producto tecnológico real  
- Hosting en GitHub Pages o Netlify  
- Documentación profesional:
  - Problema resuelto  
  - Tecnologías utilizadas  
  - Proceso de desarrollo  
  - Capturas y videos  
- Control de versiones en Git y GitHub  

---

# 🧠 Aprendizajes Clave

- Uso profesional de Django (ORM, Auth, permisos, relaciones)  
- Migraciones y manejo de bases de datos  
- CRUDs completos  
- SQL crudo y ORM  
- Bootstrap responsivo  
- Buenas prácticas de arquitectura  
- Documentación técnica  
- Despliegue de proyectos estáticos y portafolios  

---

# 📝 Cómo ejecutar los proyectos (Resumen técnico)

```bash
# 1. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 4. Ejecutar servidor
python manage.py runserver

# 5. Cargar staticfiles (proyectos con admin o media)
python manage.py collectstatic
```

---

# 📬 Contacto

Si deseas conocer más sobre este portafolio o colaborar, puedes contactarme:

✉ Email: daniel.henriquez.v@hotmail.com  
🌐 LinkedIn: https://www.linkedin.com/in/dhenriquezv/
💼 GitHub: 
