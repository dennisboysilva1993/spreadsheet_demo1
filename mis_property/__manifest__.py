# -*- coding: utf-8 -*-
{
    'name': 'Property MIS',
    'version': '0.1',
    'summary': 'Property MIS Reporting',
    'description': 'Property MIS Reporting',
    'category': 'tool',
    'author': 'Dennis Boy Silva',
    'depends': ['base',
                'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_mis.xml'
    ],
    'installable': True,
    'auto_install': False
}
