from odoo import models, fields

class SeniorProfessional(models.Model):
    _inherit = "clinicmario.professional"  # Herencia del modelo base

    years_experience = fields.Integer(string="Años de Experiencia")  # Campo adicional