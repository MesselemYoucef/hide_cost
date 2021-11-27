# -*- coding: utf-8 -*-
{
    'name': 'Hide Cost',
    'version': '1.0',
    'summary': 'Hide the product cost from some group of users',
    'sequence': -103,
    'description': """Hide the cost for a group of users""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'Licence': 'LGPL-3',
    'images': [],
    'depends': [
        'base',
        'sale',
        'product',
    ],
    'data': [
        'security/security.xml',
        'views/product_view.xml',
        'views/product_variant_view.xml',
        'views/sale_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}