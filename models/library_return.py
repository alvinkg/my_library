# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields


class LibraryBook(models.Model):
    _inherit = 'library.book'
    _description = 'Return library books'
    
    date_return = fields.Date('Date to return book.')

    day_to_borrow = fields.Integer(
        'Days to Borrow',
        related='category_id.max_borrow_days',
        readonly=True
    )

    def make_available(self):
        self.date_return = False
        return super(LibraryBook, self).make_available()

    def make_borrowed(self):
        day_to_borrow = self.category_id.max_borrow_days or 10
        self.date_return = fields.Date.today() + timedelta(days=day_to_borrow)
        return super(LibraryBook, self).make_borrowed()


class LibraryBookCategory(models.Model):
    _inherit = 'library.book.category'

    max_borrow_days = fields.Integer(
        'Maximum borrow days',
        help="For how many days book can be borrowed",
        default=10,
    )