# -*- coding: utf-8 -*-
# from odoo import http


# class OdooNueveMd(http.Controller):
#     @http.route('/odoo_nueve_md/odoo_nueve_md/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_nueve_md/odoo_nueve_md/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_nueve_md.listing', {
#             'root': '/odoo_nueve_md/odoo_nueve_md',
#             'objects': http.request.env['odoo_nueve_md.odoo_nueve_md'].search([]),
#         })

#     @http.route('/odoo_nueve_md/odoo_nueve_md/objects/<model("odoo_nueve_md.odoo_nueve_md"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_nueve_md.object', {
#             'object': obj
#         })
