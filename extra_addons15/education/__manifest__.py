{
    'name': 'Formation Technique Odoo v15',
    'version': '1.0',
    'summary': 'formation, odoo 15, erp, ',
    'description': """
        Put your description here for your module:
            - model1
            - model2
            - model3
    """,
    'category': 'Education',
    'author': 'Soumeth',
    'website': 'www.cits.com',
    'license': "AGPL-3",
    'complexity': 'easy',
    'sequence': 1,
    'depends': ['base', 'mail', 'hr', 'website', 'sale'],
    'data': ['security/formation.xml',
             'security/ir.model.access.csv',
             'views/formation_views.xml',
             'data/sequence.xml',
             'views/menu.xml',
             'controllers/formation.xml',
             'controllers/claim.xml',
             'controllers/bulletin.xml',
             'report/report.xml',
             'report/registration.xml',
             'report/bulletin_template.xml'
             ],
    'demo': [''],
    'installable': True,
    'application': True,
}