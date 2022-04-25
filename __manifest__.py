# -*- coding: utf-8 -*-
{
    'name': "learning_odoo",

    'summary': """
        Project
    """,

    'description': """
        Managing projects, accounts, jobs, partners, employees
    """,

    'author': "My Company",
    'website': "http://www.amjproductions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project-view.xml',
        'views/account-view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
