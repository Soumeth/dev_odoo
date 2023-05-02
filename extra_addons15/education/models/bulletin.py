from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Bulletin(models.Model):
    _name = 'bulletin.bulletin'

    @api.depends('note_ids')
    def _compute_average(self):
        if self.note_ids:
            average = 0
            for module in self.note_ids:
                average = average + module.average
            self.average = round(average / len(self.note_ids))

    name = fields.Char(string='Nom', readonly=True, default=lambda x: x.env['ir.sequence'].get('bulletin.bulletin'))
    year_id = fields.Many2one('year.year', string='Année')
    session_id = fields.Many2one('session.session', string='Session')
    student_id = fields.Many2one('res.partner', string='Etudiant')
    average = fields.Float(compute='_compute_average', string='Moyenne générale')
    note_ids = fields.One2many('line.bulletin', 'bulletin_id', string='Notes')
    user_id = fields.Many2one('res.users', string='Responsable')

