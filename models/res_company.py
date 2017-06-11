# -*- coding: utf-8 -*-
# Copyright 2016 Syleam
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    holidays_time_hours_id = fields.Many2one(comodel_name='product.uom',
                                             string='Holidays Hours UoM',
                                             default=lambda self: self.env.ref('product.product_uom_hour').id)
    holidays_time_days_id = fields.Many2one(comodel_name='product.uom',
                                            string='Holidays Days UoM',
                                            default=lambda self: self.env.ref('product.product_uom_day').id)
    opening_time = fields.Float(string='Opening Time', digits=(16, 2), default=8)
    closing_time = fields.Float(string='Closing Time', digits=(16, 2), default=18)
