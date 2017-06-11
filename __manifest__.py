# -*- coding: utf-8 -*-
# Copyright 2016 Syleam
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Hr Holidays Workingdays',
    'version': '10.0.1.1.0',
    'category': 'Custom',
    'summary': """Compute number of day requested without days not worked in company""",
    'author': 'SYLEAM',
    'website': 'http://www.syleam.fr/',
    'depends': [
        'base',
        'product',
        'base_workingdays',
        'hr_holidays',
    ],
    'data': [
        'views/res_company.xml',
    ],
    'installable': True,
    'auto_install': False,
    'active': False,
    'license': 'AGPL-3',
}
