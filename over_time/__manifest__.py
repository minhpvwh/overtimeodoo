# -*- coding: utf-8 -*-
{
    'name': "Overtime management",

    'summary': """
        Manage Overtime""",

    'description': """
        module OT - create by PV Minh
    """,

    'author': "PV Minh",
    'website': "http://www.erp.e-leisure.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sub module',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],
    'application': True,
    'installable': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/over_time.xml',
        'views/menu.xml',
    ],
}
