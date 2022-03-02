# -*- coding: utf-8 -*-
# from odoo import http


# class Nueve(http.Controller):
#     @http.route('/nueve/nueve/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nueve/nueve/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nueve.listing', {
#             'root': '/nueve/nueve',
#             'objects': http.request.env['nueve.nueve'].search([]),
#         })

#     @http.route('/nueve/nueve/objects/<model("nueve.nueve"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nueve.object', {
#             'object': obj
#         })
