from odoo import models, fields, api


class Technique(models.Model):
    _name= "clinicmario.technique"
    _description = "clinicmario.technique"

    id = fields.Integer()
    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")

    # En cada sesión hay varias técnicas y una técnica aparece en varias sesiones
    sessions = fields.Many2many("clinicmario.session", relation = "technique_session", column1="sessions", column2="techniques", string="Sesiones")