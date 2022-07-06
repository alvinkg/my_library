# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

logger = logging.getLogger(__name__)


class LibraryReturnWizard(models.TransientModel): # bug:  Model iso TransientModel
    _name = 'library.return.wizard'
    _description="""Return Book Wizard"""

    borrower_id = fields.Many2one('res.partner', string='Member')
    book_ids=fields.Many2many('library.book', string='Books')

    def books_returns(self):
        loanModal=self.env['library.book.rent']
        for rec in self:
            loans=loanModal.search(
                [
                    ('state','=','ongoing'),
                    ('book_id','in',rec.book_ids.ids), # bug: rec.book.ids.ids
                    ('borrower_id','=',rec.borrower_id.id)                
                ]
            )
            for loan in loans:
                loan.book_return()

    # 8.07
    @api.onchange('borrower_id')
    def onchange_member(self):
        rentModel = self.env['library.book.rent']
        books_on_rent = rentModel.search(
            [
                ('state','=','ongoing'),
                ('borrower_id','=',self.borrower_id.id)
            ]
        )
        self.book_ids=books_on_rent.mapped('book_id')

    # TODO: find out why @api.depends does not work in this odoo
    # 8.07 Onchange w/ compute mtd
    # @api.depends('borrower_id')
    # def onchange_member(self):
    #     rentModel = self.env['library.book.rent']
    #     books_on_rent = rentModel.search(
    #         [
    #             ('state','=','ongoing'),
    #             ('borrower_id','=',self.borrower_id.id)
    #         ]
    #     )
    #     book_ids = fields.Many2many(
    #         'library.book',
    #         string='Books',
    #         compute='onchange_member',
    #         readonly=False,
    #     )
    #     self.book_ids=books_on_rent.mapped('book_id')
