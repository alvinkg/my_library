{
    'name': "My Library",
    'summary': "Manage books easily",
    'description': """My Library App """,
    'author': "alvin lim",
    'website': "http://www.konvergenttech.com",
    'category': 'Library',
    'version': '14.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml',
        'views/library_book_rent.xml',
        'wizard/library_book_rent_wizard.xml',
        'data/data.xml',
        ],
    'demo': ['data/demo.xml'],
    'application': True,
    'sequence': 0,
    }

