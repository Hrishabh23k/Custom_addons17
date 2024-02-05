{
    'name': 'My Project',

    'depends': ['base','sale','project'],


    'data':[
        'security/ir.model.access.csv',
        'wizard/sale_order_wizard.xml',
        'views/sale_order.xml',
        'views/project_task.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}