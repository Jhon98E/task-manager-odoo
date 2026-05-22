{
    'name': 'Task Manager',
    'version': '1.0.0',
    'summary': 'Gestión de tareas con flujo tipo Scrum',
    'description': 'Módulo para gestionar tareas por estados: Backlog, En progreso, En revisión y Completado.',
    'author': 'Jhon David Enriquez',
    'category': 'Project',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_views.xml',
        'views/search_views.xml',
        'views/menu.xml',
        'report/task_report.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}