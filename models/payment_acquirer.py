import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('midtrans', "Midtrans")], ondelete={'midtrans': 'set default'})
    midtrans_merchant_id = fields.Char(string='Merchant ID', required_if_provider='midtrans')
    midtrans_client_key = fields.Char(string='Client Key', required_if_provider='midtrans')
    midtrans_server_key = fields.Char(string='Server Key', required_if_provider='midtrans', groups='base.group_system')