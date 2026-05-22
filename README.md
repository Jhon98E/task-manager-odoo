# Task Manager - Módulo Odoo 19

Módulo personalizado para Odoo 19 que permite gestionar tareas con un flujo de trabajo tipo Scrum.

## Funcionalidades

- Tablero Kanban con columnas: Backlog, En progreso, En revisión, Completado
- Vista Lista y Formulario
- Gestión de prioridades (Normal, Importante, Urgente) con colores en Kanban
- Asignación de responsables
- Fechas límite
- Filtros por estado y prioridad
- Agrupaciones por estado, prioridad, responsable y fecha
- Historial de cambios de estado (Chatter)
- Validación: no se puede completar una tarea sin descripción
- Reporte PDF imprimible con QWeb
- Datos de demo precargados

## Tecnologías

- Odoo 19 Community
- Python 3
- XML (vistas QWeb)
- PostgreSQL

## Requisitos del sistema

- Odoo 19 Community
- wkhtmltopdf (para generación de reportes PDF)
  - Windows: https://wkhtmltopdf.org/downloads.html
  - Linux: `sudo apt install wkhtmltopdf`

## Instalación

1. Clonar el repositorio en la carpeta de addons personalizados
2. Agregar la ruta en `odoo.conf`
3. Reiniciar Odoo
4. Activar modo desarrollador
5. Actualizar lista de módulos
6. Instalar **Task Manager**

## Autor

Jhon David Enriquez
Desarrollador de Software