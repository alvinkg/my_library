# -*- coding: utf-8 -*-

from odoo import models, fields


class Librarybook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'
    short_name = fields.Char('Short Title', required=True)
    
    name=fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many(
        'res.partner',
        string='Authors'
)

    # def name_get(self):
    #     """This method used to customized the display name of the record"""
    #     result=[]
    #     for record in self:
    #         rec_name='%s (%s)' % (record.name, record.date_release)
    #         result.append(record.id, rec_name)
    #     return result
    
    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
            result.append((record.id, rec_name))
        return result