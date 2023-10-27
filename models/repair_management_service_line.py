from odoo import fields, models, api, _

class RepairManagementServiceLine(models.Model):
    _name = 'pj.repair.management.service.line'
    _description = 'Repair Management Service Line'

    repair_id = fields.Many2one('pj.repair.management', string="Repair")
    product_id = fields.Many2one('product.product', string="Product")
    uom_id = fields.Many2one('uom.uom', string="UOM")
    name = fields.Char(string="Name")
    qty = fields.Integer(string="Quantity")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('received', 'Received'),
        ('repairing', 'Repairing'),
        ('invoicing', 'Invoicing'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
       ], string="Status")
    price_unit = fields.Float(string="Unit Price")
    amount = fields.Float(string="Amount", compute='_compute_amount')


    @api.depends('qty', 'price_unit')
    def _compute_amount(self):
        for record in self:
            record.amount = record.qty * record.price_unit
