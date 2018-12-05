# -*- coding: utf-8 -*-

from odoo import fields, models, api
import time


class Overtime(models.Model):
    _name = 'hr.overtime'

    _rec_name = 'target'

    create_day = fields.Date("Overtime day", default = lambda *a: time.strftime('%Y-%m-%d'), required = True)
    target = fields.Char("Target", required = True)
    payroll = fields.Selection(string = "Payroll",
                               selection = [('payroll_yes', 'Yes'), ('payroll_no', 'No')], default = 'payroll_no')
    subsidy = fields.Integer("Subsidy")
    note = fields.Text("Note")

    emp = fields.One2many("overtime.sub", 'ot')

    index = fields.Float("Index")

    @api.model
    def auto_department(self):
        resource = self.env['resource.resource'].search([('user_id', '=', self.env.user.id)])

        employee = self.env['hr.employee'].search([('resource_id', '=', resource.id)])

        department = employee.department_id

        return department

    department_id = fields.Many2one("hr.department", "Department", default = auto_department)


class Subovertime(models.Model):
    _name = 'overtime.sub'

    ot = fields.Many2one("hr.overtime")

    emp = fields.Many2one("hr.employee", "Name Employee")
    time_ot = fields.Integer("Time Overtime")
    eat_lunch = fields.Boolean("Eat Lunch")
    day_ot = fields.Date("Day Overtime", relate = "ot.create_day")
    note = fields.Text("Note")
    rate = fields.Selection([(1, 'Bad'), (2, 'Nomal'), (3, 'Good'), (4, 'Very Good')],
                            string = "Rating", default = 2)
