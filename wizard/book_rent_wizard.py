# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryRentWizard(models.Model): # 8.04.1
    _name='library.rent.wizard'
    _description="Rent Wizard"

    borrower_id = fields.Many2one('res.partner', string='Borrower')
    book_ids= fields.Many2many('library.book', string='Books')

    # 8.04.2
    def add_book_rents(self):
        # an empty recordset of library.book.rent
        rentModel = self.env['library.book.rent']

        for wiz in self:
            for book in wiz.book_ids:
                rentModel.create({
                    'borrower_id': wiz.borrower_id.id,
                    'book_id': book.id,
                })
                
        borrowers = self.mapped('borrower_id')
        action = borrowers.get_formview_action()
        if len(borrowers.ids)>1:
            action['domain']=[('id', 'in', tuple(borrowers.ids))]
            action['view_mode']='tree,form'
        return action
