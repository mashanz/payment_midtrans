import logging
import pprint

import requests

from odoo import _, http
from odoo.exceptions import ValidationError
from odoo.http import request

_logger = logging.getLogger(__name__)


class MidtransController(http.Controller):
    _payment_notification_url = '/payment/midtrans/payment_notification'
    _recurring_notification_url = '/payment/midtrans/recurring_notification'
    _pay_account_notification_url = '/payment/midtrans/pay_account_notification'
    _finish_url = '/payment/midtrans/finish'
    _unfinish_url = '/payment/midtrans/unfinish'
    _error_url = '/payment/midtrans/error'

    @http.route(_payment_notification_url, type='http', auth='public', methods=['POST'], csrf=False)
    def midtrans_payment_notification(self, **post):
        pass

    @http.route(_recurring_notification_url, type='http', auth='public', methods=['POST'], csrf=False)
    def midtrans_recurring_notification(self, **post):
        pass

    @http.route(_pay_account_notification_url, type='http', auth='public', methods=['POST'], csrf=False)
    def midtrans_pay_account_notification(self, **post):
        pass

    @http.route(_finish_url, type='http', auth='public', methods=['POST'], csrf=False)
    def midtrans_finish(self, **post):
        pass

    @http.route(_unfinish_url, type='http', auth='public', methods=['POST'], csrf=False)
    def midtrans_unfinish(self, **post):
        pass

    @http.route(_error_url, type='http', auth='public', methods=['POST'], csrf=False)
    def midtrans_error(self, **post):
        pass