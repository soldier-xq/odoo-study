# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "dj",
    'category': 'Category',
    'description': """
        Estate module description
    """,
    'data': [
        "security/ir.model.access.csv",
        "views/templates.xml",
        "views/estate_property_views_tag.xml",
        "views/estate_property_views.xml",
        "views/estate_property_views_type.xml",
        "views/estate_property_views_offer.xml",
        "views/estate_menus.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    "license": "LGPL-3",
}