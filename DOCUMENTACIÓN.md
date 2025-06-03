# 📄 Documentación Técnica – Prueba Desarrollador Full Stack

---

## a. Descripción de la arquitectura de la solución

La solución está compuesta por dos aplicaciones separadas: **frontend** y **backend**, desarrolladas de forma desacoplada para facilitar la escalabilidad, modularidad y despliegue independiente.

### 🔹 Frontend
- Framework: **Angular** utilizando `standalone components`.
- Integración con **Ionic** para asegurar compatibilidad multiplataforma (Android/iOS/web).
- Componentes reutilizables y estructura modular distribuida así:
  - `categories/pages/`: vistas para gestión de categorías.
  - `components/`: componentes compartidos como modales y formularios.
  - `core/`: modelos, servicios y lógica común.
  - `home/`: vista principal donde se visualizan y gestionan tareas.

### 🔹 Backend
- Framework: **Django REST Framework**.
- API RESTful con endpoints CRUD para tareas y categorías.
- Base de datos: **Firebase Firestore** (NoSQL).
- Conexión segura mediante `firebase-admin-sdk` y autenticación por clave privada.
- Organización en:
  - `manager/`: vistas, serializadores, modelos y routers.
  - `ionic_todo_backend/`: configuración general del proyecto.
  - `config/firebase-credentials.json`: archivo de credenciales para conexión con Firebase.

---

## b. Instrucciones para ejecutar localmente

Todos los pasos de ejecución están detallados en los archivos `README.md` de cada repositorio. Se recomienda el uso de **Docker** para levantar el entorno sin instalar dependencias manualmente.

### 🔧 Requisitos:
- Tener **Docker** y **Docker Compose** instalados.
- Verificar que los puertos `8000` (backend) y `8100` (frontend) estén libres.
- Crear una carpeta `config/` en el backend y ubicar dentro el archivo `firebase-credentials.json`.

### ▶️ Despliegues disponibles:

- **Frontend**: [http://89.116.26.26:8100/home](http://89.116.26.26:8100/home)
- **Backend (API)**: [http://89.116.26.26:8000/api/](http://89.116.26.26:8000/api/)
- **Swagger (API Docs)**: [http://89.116.26.26:8080/swagger-ui/index.html](http://89.116.26.26:8080/swagger-ui/index.html)

---

## c. Decisiones técnicas clave

Durante el desarrollo se tomaron múltiples decisiones técnicas estratégicas para optimizar el tiempo, mantener buenas prácticas y garantizar funcionalidad:

### 🔹 Elección de tecnologías
- **Angular + Ionic**: Aunque domino React, opté por Angular por fluidez de desarrollo en corto tiempo. Con Ionic pude generar una app móvil con Cordova, la tecnología que más manejo para empaquetado Android.
- **Django REST Framework**: Fue ideal para exponer rápidamente una API REST, cumplir con el uso de Python y aprovechar la productividad que brinda este framework para operaciones CRUD.

### 🔹 Arquitectura y modularidad
- Se usaron componentes standalone y compartidos para tareas y categorías, facilitando el mantenimiento.
- El backend se diseñó con separación clara entre lógica de negocio, rutas y controladores.

### 🔹 Contenerización y despliegue
- El uso de Docker fue clave para asegurar un entorno idéntico entre desarrollo local y producción.
- Esto también permitió desplegar fácilmente el proyecto en servidores Linux y facilitar pruebas sin necesidad de instalar dependencias en el equipo del evaluador.

### 🔹 Persistencia NoSQL
- La integración con Firebase Firestore, como base de datos no relacional, fue un reto interesante. Requirió adaptar el diseño clásico relacional de Django a una estructura de documentos, cuidando los IDs y referencias para garantizar consistencia.

### 🔹 Reutilización
- Se implementaron modales reutilizables, validaciones de formularios, servicios compartidos y filtros personalizados, lo cual aumentó la mantenibilidad del código.

### 🔹 Control de versiones y enfoque incremental
- Se siguió un enfoque de desarrollo incremental (mínimos viables), aplicando refactorizaciones iterativas y commits significativos.
- Cada funcionalidad añadida fue registrada y validada por separado.

---

## d. Enfoque bajo metodología Scrum

El desarrollo siguió un enfoque similar a un flujo Scrum simplificado:

- **Backlog**: Se definieron las funcionalidades prioritarias y se desarrollaron por entregables funcionales (MVP).
- **Iteraciones**:
  - Primera iteración: creación de tareas con título y categoría.
  - Segunda: adición de estado, descripción, edición y eliminación.
  - Tercera: validaciones, filtros por categoría, mejoras de UI.
  - Cuarta: persistencia en localStorage, luego integración con backend, y finalmente con Firebase.
- **Commits por funcionalidad**: cada etapa o refactor quedó reflejada en el historial de Git, asegurando trazabilidad.
- **Automatización**: se sentaron bases para implementar CI/CD aprovechando la contenerización (tarea que podría automatizarse en GitHub Actions).
- En un entorno real, se habría usado JIRA para organizar tareas, planificación de sprints, revisión de Pull Requests y pruebas automatizadas.

---

## ⏱ Tiempo estimado de dedicación

El desarrollo total del proyecto se distribuyó de la siguiente forma:

- **Domingo**: ~7 horas → Desarrollo del frontend, diseño UI/UX e inicio del backend.
- **Lunes**: ~8 horas → Finalización backend, integración completa, despliegue y contenedores.
- **Martes**: ~2 horas → Documentación, ajustes finales y entrega.

**Total estimado: ~17 horas de trabajo efectivo.**

---

## ✍️ Autor

**Juan Pablo Herrera Herrera**  
[GitHub – Juanpabloxv](https://github.com/Juanpabloxv)

---
