# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_sale_order(models.Model):
    _inherit = 'sale.order'
    # paid = fields.Char('Paid')
    # remaining = fields.Char('Remaining')
    # payment_schedule = fields.Char('Payment Schedule')





