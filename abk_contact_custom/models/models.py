# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_res_partner(models.Model):
    _inherit = 'res.partner'
    customer_no = fields.Char('Customer Number')
    name_chinese = fields.Char('Chinese Name')
    name_english = fields.Char('English Name')
    address_chinese = fields.Text('Chinese Address')
    address_english = fields.Text('English Address')
    fax = fields.Char('Fax')
    attention = fields.Char('Attention')
    invattn = fields.Char('Invoice Attention')
    contact = fields.Char('Contact')
    paydesc = fields.Text('Payment Description')
    remark = fields.Text('Remark')
    monthpay = fields.Char('Month pay')
    currency = fields.Many2one("res.currency", string="Currency")
    crlimit = fields.Char('Credit limit')
    discnt = fields.Char('Discount')
    sales_code = fields.Char('Sales Code')
    invdiscnt = fields.Char('Invoice Discount')
    chiadd = fields.Char('Chiadd')
    lang_use = fields.Selection([('english', 'E'), ('chinese', 'C')], string="Language")
    payterm = fields.Selection([('option_1', '0'), ('option_2', '7'),
                                ('option_3', '15'), ('option_4', '20'),
                                ('option_5', '30'), ('option_6', '45'),
                                ('option_7', '60'), ('option_8', '90')], string="Payterm")





