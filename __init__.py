from . import models
from . import controllers
from . import wizard
from odoo import api, fields, SUPERUSER_ID

# 8.10.2 Add mtd and import a/r
def add_book_hook(cr,registry): #mtd is post_init call
    env=api.Environment(cr, SUPERUSER_ID, {})
    book_data1 = {'name': 'Days of Our Lives', 'short_name': 'Days', 'date_release':fields.Date.today()}
    book_data2 = {'name': 'Dallas', 'short_name': 'Dallas', 'date_release':fields.Date.today()}
    env['library.book'].create([book_data1, book_data2])