# -*- coding: utf-8 -*-

from odoo import fields, models


class Overtime(models.Model):
    _name = 'over.time'


    create_day =  fields.Datetime("Create day")
    target      = fields.Char("Target")
    tinhluong = fields.Integer("Tính Luong?")
    phuphi = fields.Integer("Phụ phí")
    note = fields.Text("Note")
    soluongnv = fields.Integer("So lương nhân viên")



    #emp = fields.Many2many(comodel_name="res.user",string="Tên Nhân Viên")


    time_ot = fields.Integer("Sô giờ làm thêm")
    scheduled = fields.Text("Quy trình sử dụng phụ phí")