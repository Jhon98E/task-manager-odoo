from odoo import models, fields, api

class TaskManager(models.Model):
    _name = 'task.manager'
    _description = 'Tarea'
    _order = 'priority desc, deadline asc'

    name = fields.Char(string='Tarea', required=True)
    description = fields.Text(string='Descripción')
    responsible_id = fields.Many2one('res.users', string='Responsable', default=lambda self: self.env.user)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Importante'),
        ('2', 'Urgente'),
    ], string='Prioridad', default='0')
    deadline = fields.Date(string='Fecha límite')
    state = fields.Selection([
        ('backlog',     'Backlog'),
        ('in_progress', 'En progreso'),
        ('review',      'En revisión'),
        ('done',        'Completado'),
    ], string='Estado', default='backlog')
    color = fields.Integer(string='Color')

    def action_start(self):
        self.state = 'in_progress'

    def action_review(self):
        self.state = 'review'

    def action_done(self):
        self.state = 'done'

    def action_reset(self):
        self.state = 'backlog'