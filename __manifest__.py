# -*- coding: utf-8 -*-
{
    'name': "pj_repair_management",

    'summary': """
        Repair_Management""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'sale'],

    # always loaded
    'data': ['views/repair_management_view.xml',
             'views/repair_service_line_view.xml',
             'views/product_repair_management_view.xml',
             ],
    # only loaded in demonstration mode
    'demo': [],

}
