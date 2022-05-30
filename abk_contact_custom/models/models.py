# -*- coding: utf-8 -*-

from odoo import models, fields, api

class custom_res_partner(models.Model):
    _inherit = 'res.partner'
    name_chinese = fields.Char('Chinese Name')
    name_english = fields.Char('English Name')

    # Chinese Address Fields
    chinese_street = fields.Char('Street', readonly=False, store=True)
    chinese_street2 = fields.Char('Street2', readonly=False, store=True)
    chinese_zip = fields.Char('Zip', change_default=True, readonly=False, store=True)
    chinese_city = fields.Char('City', readonly=False, store=True)
    chinese_state_id = fields.Many2one(
        "res.country.state", string='State', readonly=False, store=True,
        domain="[('country_id', '=?', country_id)]")
    chinese_country_id = fields.Many2one(
        'res.country', string='Country', readonly=False, store=True)

    # English Address Fields
    english_street = fields.Char('Street', readonly=False, store=True)
    english_street2 = fields.Char('Street2', readonly=False, store=True)
    english_zip = fields.Char('Zip', change_default=True, readonly=False, store=True)
    english_city = fields.Char('City', readonly=False, store=True)
    english_state_id = fields.Many2one(
        "res.country.state", string='State', readonly=False, store=True,
        domain="[('country_id', '=?', country_id)]")
    english_country_id = fields.Many2one(
        'res.country', string='Country', readonly=False, store=True)
