from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Module(models.Model):
    _name = 'module.module'
    _description = 'modules'

    name = fields.Char(string='Unité fondamentale', required=True)
    code = fields.Char(string='Code', required=True)
    credits = fields.Integer(string="credits", required=True)
    description = fields.Text(string='Description')
    section_id = fields.Many2one('section.section', string='Section')
    matiere_ids = fields.One2many('matiere.matiere', 'module_id', string='Matiere')

    _sql_constraints = [
        ('code', 'unique(code)',
         "Ce code existe déjà pour un autre module !"),
    ]


class Matiere(models.Model):
    _name = 'matiere.matiere'
    _description = 'matieres'

    name = fields.Char(string='Matière', required=True)
    code = fields.Char(string='Code', required=True)
    module_id = fields.Many2one('module.module', string='Module')

    _sql_constraints = [
        ('code', 'unique(code)',
         "Ce code existe déjà pour une autre matière !"),
    ]
