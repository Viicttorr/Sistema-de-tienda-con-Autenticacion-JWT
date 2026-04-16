# 🛒 Sistema de tienda con Autenticación JWT

Aplicación web desarrollada en **Django** como parte de la Evaluación Sumativa 4 de Programación Back End.  
El proyecto consiste en una **tienda online** con un **Backend en Django** que expone una **API REST** para consultar productos, aplicando seguridad con **JWT** y conexión a un **Frontend externo**.

---

## 🚀 Funcionalidades principales

- **Backend con Django**:
  - Proyecto: `tienda`
  - App: `productos`
  - Carpeta `api` con funcionalidades de la API
- **Modelo Producto** con campos:
  - Título (máx. 100 caracteres)
  - Precio (entero positivo)
  - Descripción (texto largo)
  - Imagen (URL)
  - Categoría (string máx. 100 caracteres)
- **Base de datos SQLite** con migraciones aplicadas.
- **API REST** con endpoints:
  - `http://127.0.0.1:8000/api/producto` → Vista simple
  - `http://127.0.0.1:8000/api/productos/` → Vista compleja
  - `http://127.0.0.1:8000/api/token/` → Obtención de token JWT
- **Seguridad con JWT** usando `djangorestframework-simplejwt`.
- **CORS habilitado** con `django-cors-headers`.

---

## 🎯 Objetivos de aprendizaje

1. Desarrollar una **API REST** con Django y Django Rest Framework.  
2. Implementar autenticación con **JWT**.  
3. Configurar **CORS** para permitir conexión con frontend externo.  
4. Exponer endpoints seguros para consulta de productos.  
5. Conectar el backend con un **frontend proporcionado por el docente**.  

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **Django**
- **Django Rest Framework**
- **djangorestframework-simplejwt**
- **django-cors-headers**
- **SQLite**
- **Visual Studio Code (Thunder Client para pruebas)**

---

## 📂 Estructura del proyecto

- `/tienda/` → Configuración principal del proyecto.  
- `/productos/` → App con modelos y lógica de negocio.  
- `/api/` → Endpoints y vistas de la API.  
- `/frontend/` → Carpeta con `index.html` para consumir la API.  

---

## ⚙️ Instalación y ejecución

1. Clonar el repositorio.
2. Crear y activar entorno virtual:
   - python -m venv venv
   - venv\Scripts\activate.bat
3. Instalar dependencias:
   - pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
5. Ejecutar servidor:
   - python manage.py runserver
6. Abrir en navegador:
   - http://127.0.0.1:8000/

---

## 🔑 Pruebas con JWT
- En la carpeta frontend abrir con el navegador index.html
   - Producto aleatorio: consultas sin token a la base de datos.
   - Todos(token): usar extensión Thunder Client en VS Code para solicitar y almacenar el token.
- El frontend (index.html) mostrará productos solo si el token es válido.
- En caso de no tener token, los datos no se mostrarán.

---

## 👨‍💻 Actividad demostrada
- Creación de API REST con Django Rest Framework.
- Implementación de modelo Producto y migraciones en SQLite.
- Configuración de endpoints para consulta de productos.
- Seguridad con JWT y configuración de CORS.
- Conexión con frontend externo para visualizar productos.

---

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT.
Puedes usarlo, modificarlo y compartirlo libremente, siempre mencionando la autoría original.
