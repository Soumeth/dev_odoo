from . import models, fields


class AgenceVehicule(models.Model):
    _name = 'agence.vehicule'
    # Les caractéristiques des véhicules
    marque = fields.Char('Marque', required=True)
    modele = fields.Char('Modèle', required=True)
    date_achat = fields.Date('DateAchat')
    chaffeur_ids = fields.Many2many(
        'res.partner',
        string='Chauffeurs'
    )