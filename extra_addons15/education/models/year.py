from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class Year(models.Model):
    _name = 'year.year'
    _description = 'Academic Year'
    _rec_name = 'name'

    name = fields.Char(string='Nom', required=False, readonly=False, help='Name of academic year')
    code = fields.Char(string='Code', required=False, readonly=False)
    start_date = fields.Date('Date début', required=True, help='Starting date of academic year')
    end_date = fields.Date('Date fin', required=True, help='Ending of academic year')
    description = fields.Text(string='Description', help="Description about the academic year")
    session_ids = fields.One2many('session.session', 'year_id', string='Session')
    active = fields.Boolean(
        'Active', default=True,
        help="If unchecked, it will allow you to hide the Academic "
             "Year without removing it.")

    _sql_constraints = [
        ('code', 'unique(code)',
         "Ce code existe déjà pour une autre année académique !"),
    ]

    @api.constrains('start_date', 'end_date')
    def validate_date(self):
        """" cette fonction teste si La date de debut est antérieure à la date de fin """""
        for rec in self:
            if rec.start_date >= rec.end_date:
                raise ValidationError(
                    _('La date de début doit être antérieure à la date de fin'))
