# -*- coding: utf-8 -*-
from odoo import http

# class Over-time(http.Controller):
#     @http.route('/over-time/over-time/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/over-time/over-time/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('over-time.listing', {
#             'root': '/over-time/over-time',
#             'objects': http.request.env['over-time.over-time'].search([]),
#         })

#     @http.route('/over-time/over-time/objects/<model("over-time.over-time"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('over-time.object', {
#             'object': obj
#         })