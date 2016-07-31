# -*- coding: utf-8 -*-
##############################################################################
#
#    hr_holidays_workingdays module for OpenERP, Compute number of day requested without days not worked in company
#    Copyright (C) 2016 SYLEAM Info Services (<http://www.syleam.fr>)
#              Sebastien LANGE <sebastien.lange@syleam.fr>
#
#    This file is a part of hr_holidays_workingdays
#
#    hr_holidays_workingdays is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    hr_holidays_workingdays is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.model
    def _get_uom_hours(self):
        try:
            return self.env.ref("product.product_uom_hour")
        except ValueError:
            return False

    @api.model
    def _get_uom_days(self):
        try:
            return self.env.ref("product.product_uom_day")
        except ValueError:
            return False

    holidays_time_hours_id = fields.Many2one('product.uom', string='Holidays Hours UoM', default=_get_uom_hours)
    holidays_time_days_id = fields.Many2one('product.uom', string='Holidays Days UoM', default=_get_uom_days)
    opening_time = fields.Float(string='Opening Time', digits=(16, 2), default=8, )
    closing_time = fields.Float(string='Closing Time', digits=(16, 2), default=18, )


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
