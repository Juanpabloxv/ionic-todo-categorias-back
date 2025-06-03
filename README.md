# ionic-todo-categorias-back

API REST backend para la aplicación To-Do List, desarrollada con Django REST Framework, conectada a Firebase como base de datos NoSQL y contenerizada con Docker para facilitar el despliegue.

---

## 🔍 Descripción

Este backend proporciona los endpoints necesarios para:

- Crear, consultar, actualizar y eliminar tareas.
- Crear, consultar, actualizar y eliminar categorías.
- Asignar tareas a categorías.
- Mantener sincronización con Firebase como base de datos no relacional.

Además, se encuentra **totalmente contenerizado** con Docker, permitiendo que se levante fácilmente sin necesidad de instalar dependencias manuales.

---

## ⚙️ Tecnologías

- **Python 3.11**
- **Django 4**
- **Django REST Framework**
- **Firebase Admin SDK**
- **Docker & Docker Compose**

---

## 📂 Estructura principal

- `manager/` → App principal con vistas, modelos y rutas.
- `ionic_todo_backend/` → Proyecto base Django.
- `config/firebase-credentials.json` → Credenciales para conexión con Firebase.
- `Dockerfile` y `docker-compose.yml` → Archivos de configuración para contenerización.

---

## 🔐 Configuración de Firebase

Para que la aplicación funcione correctamente, debes crear y conectar tu propio proyecto de Firebase. Esto asegura que cada usuario tenga control total sobre sus datos y configuración.

1. Crea un proyecto en [Firebase Console](https://console.firebase.google.com/).
2. Activa Firestore en modo producción o prueba.
3. Crea una nueva clave para una cuenta de servicio:
   - Ve a **Configuración del proyecto > Cuentas de servicio**
   - Haz clic en "Generar nueva clave privada"
   - Guarda el archivo `.json`

4. Renombra ese archivo a `firebase-credentials.json` y colócalo en la carpeta `config/` del proyecto.

## 🚀 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/Juanpabloxv/ionic-todo-categorias-back.git
cd ionic-todo-categorias-back
```

### 2. Ejecutar con Docker

Asegúrate de tener Docker instalado y activo:

```bash
docker-compose up --build
```

Esto construirá y levantará automáticamente el backend en `http://localhost:8000`.

> ⚠️ Asegúrate de ejecutar este comando en la misma ruta donde está el archivo `docker-compose.yml`.


### 3. Detener la Aplicación

```bash
docker-compose down
```

Si deseas eliminar volúmenes y reiniciar todo:

```bash
docker-compose down --volumes
---

## 🌐 Despliegue en la nube

Puedes consultar el aplicativo backend desplegado en la siguiente URL:

**👉 [http://89.116.26.26:8000/](http://89.116.26.26:8000/)**

Este servicio está preparado para ser desplegado en entornos cloud como:
- Render
- Railway
- Azure App Service
- DigitalOcean App Platform

> **Nota:** Solo necesitas establecer las variables de entorno necesarias y cargar el archivo `firebase-credentials.json`.

---

## 📌 Consideraciones

- Puedes utilizar el backend directamente con `python manage.py runserver`, pero **se recomienda usar Docker** para mantener el entorno controlado.
- El backend se comunica directamente con Firebase (Firestore) como base de datos.

## Contribuciones

Puedes contribuir con mejoras, reportar errores o sugerir nuevas funcionalidades en el [repositorio de GitHub](https://github.com/Juanpabloxv/ionic-todo-categorias-back).

---

## Licencia

Creado por: Juan Pablo Herrera Herrera