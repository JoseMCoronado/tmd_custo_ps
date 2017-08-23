# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'TMD Holdings Customizations/Developments',
    'category': 'Sale',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Core workflow customizations/developments
        """,
    'depends': ['base','stock','product'],
    'data': [
        'data/ir_model_fields.xml',
        'data/ir_ui_views.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_menu.xml',
    ],
    'installable': True,
    'application': True,
}
