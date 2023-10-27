from odoo import fields, models, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    pj_repair_id = fields.Many2one('pj.repair.management', string='Repair')
    repair_description = fields.Char(string="Description Repair")