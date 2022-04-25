from odoo import models, fields, api, _

class Job(models.Model):
    _name = 'learning_odoo.job'
    _description = 'Job'

    title = fields.Char(string="Title", required=True)
    projects_ids = fields.Many2one('learning_odoo.project', string='Project')