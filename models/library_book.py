from odoo import models, fields
class Librarybook(models.Model):
    _name = 'library.book'

    name=fields.Char('Title', Required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many(
        'res.partner',
        string='Authors'
)