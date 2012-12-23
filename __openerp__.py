# -*- coding: utf-8 -*-
##############################################################################
#
#    hr_holidays_workingdays module for OpenERP, Compute days of holiday depending working days
#    Copyright (C) 2012 SYLEAM Info Services (<http://www.syleam.fr/>)
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
    'name': 'Hr Holidays Working Days',
    'version': '1.0',
    'category': "Human Resources",
    'complexity': "easy",
    'description': """
Compute days of holiday depending working days
    """,
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'depends': [
        'base',
        'base_workingdays',
        'hr_holidays',
    ],
    'init_xml': [],
    'images': [],
    'update_xml': [
    ],
    'demo_xml': [],
    'test': [],
    #'external_dependancies': {'python': ['kombu'], 'bin': ['which']},
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
