# Proyecto de Notificaciones en Django

Este es un proyecto simple de Django que proporciona un backend para gestionar notificaciones. Incluye endpoints para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre notificaciones, así como funcionalidades adicionales.

## Configuración del Proyecto

### Requisitos Previos

- Python 3.x
- Django 3.x

### Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL del repositorio>
   cd notificaciones_project
   ```

2. Crea un entorno virtual (opcional, pero se recomienda):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En sistemas basados en Unix
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Realiza migraciones para crear la base de datos:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

El proyecto estará disponible en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Endpoints API

- **Listar Notificaciones:** `GET /notificaciones/listar/`
- **Eliminar Notificación:** `GET /notificaciones/eliminar/<int:notif_id>/`
- **Actualizar Estado Leído:** `GET /notificaciones/actualizar_leido/<int:notif_id>/`
- **Actualizar Estado Leído en Lote:** `POST /notificaciones/actualizar_leido_en_lote/`
- **Lista Resumen de Notificaciones:** `GET /notificaciones/lista_resumen/`
- **Contador de Mensajes por Leer:** `GET /notificaciones/contador_mensajes_por_leer/`
- **Crear Notificación:** `POST /notificaciones/crear_notificacion/`

## Panel de Administración

Puedes acceder al panel de administración de Django en [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) para gestionar las notificaciones.

- Usuario: admin
- Contraseña: admin

## Contribuciones

Si encuentras errores o mejoras posibles, ¡no dudes en contribuir! Abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
