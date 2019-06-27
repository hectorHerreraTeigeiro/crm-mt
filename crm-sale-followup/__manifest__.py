# -*- coding: utf-8 -*-
{
    'name': "crm-sale-followup",

    'summary': """
        Adds fields and logic for Sale followup in crm""",

    'description': """
        Adds fields and logic for Sale followup in crm
    """,

    'author': "mtNet",
    'website': "http://www.mtnet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'crm',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}