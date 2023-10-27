from odoo import fields, models, api, _
from odoo.exceptions import UserError


class RepairManagement(models.Model):
    _name = 'pj.repair.management'
    _description = 'Repair Managerment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    partner_id = fields.Many2one('res.partner', string="Partner")
    reference = fields.Char(string='Order Reference', required=False, copy=False, readonly="1", index=True,
                            default=lambda self: _('PR'))
    partner_code = fields.Char(string="Partner Code")
    partner_name = fields.Char(string="Partner Name")
    machine_name = fields.Char(string="Machine Name")
    machine_serial = fields.Char(string="Machine Serial")
    machine_info = fields.Text(string="Machine Info")
    receive_date = fields.Date(string="Receive Date")
    return_date = fields.Date(string="Return Date")
    start_date_warranty = fields.Date(string="Start Date")
    end_date_warranty = fields.Date(string="End Date")
    used_id = fields.Many2one('res.users', string="ID User")
    note = fields.Text(string="Description")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('received', 'Received'),
        ('repairing', 'Repairing'),
        ('invoicing', 'Invoicing'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
       ], string="Status", default='draft', readonly=True, copy=False, Tracking=True, track_visibility='onchange')
    amount_total = fields.Float(string='Total Amount', compute='_compute_amount_total')
    invoice_count = fields.Integer(string='Invoice Count', compute='_compute_invoice_count')
    invoice_ids = fields.One2many('account.move', 'pj_repair_id', string='Invoices')
    repair_management_ids = fields.One2many('pj.repair.management.service.line', 'repair_id', string="Repair Management")

    @api.model
    def create(self, values):
        values['reference'] = self.env['ir.sequence'].next_by_code('pj.repair.management')
        return super(RepairManagement, self).create(values)

    def _compute_amount_total(self):
        for record in self:
            total = sum(record.invoice_ids.mapped('amount_total'))
            record.amount_total = total

    def _compute_invoice_count(self):
        for record in self:
            record.invoice_count = len(record.invoice_ids)

    def unlink(self):
        for request in self:
            if request.state != 'draft':
                raise UserError(_("You can only delete purchase requests in draft state."))
        return super(RepairManagement, self).unlink()

    def request_approval(self):
        for order in self:
            if order.state not in ['draft', 'sent']:
                continue
            else:
                order.write({'state': 'invoicing'})

    def action_set_draft(self):
        self.write({'state': 'draft'})
        return {}

    def action_set_done(self):
        for order in self:
            if order.state == 'invoicing':
              order.write({'state': 'cancel'})
        return True
