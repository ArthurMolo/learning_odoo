from odoo import models, fields, api, _

class Account(models.Model):
    _name = 'learning_odoo.account'
    _description = 'Account'

    number = fields.Char(string="Number", required=True)
    project_id = fields.Many2one('learning_ooo.project', string='Projects')
    amount = fields.Char(string="Amount", required=True)
