# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _name = 'learning_odoo.project'
    _description = 'Project'

    title = fields.Char(string="Title", required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(string='End Date')
    client_id = fields.Many2one('res.partner', string='Client')
    manager_id = fields.Many2one('hr.employee', string='Manager', domain=[('manager', '=', True)])
    employees_ids = fields.Many2many('hr.employee', string='Employees')
    # job_ids = fields.One2many('learning_odoo.job', 'project_id', string='Jobs')
    # account_ids = fields.One2many('learning_odoo.account', 'project_id', string='Accounts')



#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
