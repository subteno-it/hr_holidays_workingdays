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

{
    'name': 'Hr Holidays Workingdays',
    'version': '1.0',
    'category': 'Custom',
    'description': """Compute number of day requested without days not worked in company""",
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'depends': [
        'base',
        'base_workingdays',
        'hr_holidays',
    ],
    'data': [
        'views/res_company.xml',
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
