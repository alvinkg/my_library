# -*- coding: utf-8 -*-
import logging
from re import X

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.translate import _


class LibraryBookRent(models.Model):
    _name = 'library.book.rent'
    _description = 'For Book Rentals'

    book_id = fields.Many2one('library.book', 'Book', required=True)
    borrower_id = fields.Many2one('res.partner', 'Borrower', required=True)
    #8.02.1
    state = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
        ('lost', 'Lost'),
        ],
        'State', default='ongoing', required=True)
    rent_date = fields.Date(default=fields.Date.today)
    return_date = fields.Date()

    #5.02.3
    def book_lost(self):
        #5.02.4
        self.ensure_one()
        self.sudo().state = 'lost'
        #5.02.5
        # book_with_different_context = self.book_id.with_context(avoid_deactivate=True)
        # book_with_different_context.sudo().make_lost()
        #5.02.5.1
        new_context = self.env.context.copy() #create a copy of the context
        new_context.update({'avoid_deactivate':True}) # update with new key-value
        book_with_different_context = self.book_id.with_context(new_context) # pass dict new_context
        book_with_different_context.sudo().make_lost()

    # Added code to actually return books
    def book_return(self):
        self.ensure_one()
        self.state = 'returned'

    # TODO: return book status update in library.book too