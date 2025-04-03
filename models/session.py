from odoo import models, fields, api


class Session(models.Model):
    _name= "clinicmario.session"
    _description = "clinicmario.session"

    id = fields.Integer()
    name = fields.Char(required = True, string="Nombre")
    description = fields.Text(string="Descripción")
    date = fields.Date(string="Fecha")

    # Un tratamiento puede tener varias sesiones y cada sesión tiene un único tratamiento
    treatment = fields.Many2one("clinicmario.treatment", ondelete = "CASCADE", string="Tratamientos")

    # En cada sesión hay varias técnicas y una técnica aparece en varias sesiones
    techniques = fields.Many2many("clinicmario.technique", relation = "technique_session", column1="techniques", column2="sessions", string="Técnicas")

    professional = fields.Many2one("clinicmario.professional", ondelete="CASCADE", string="Profesional", readonly=True, compute="_get_professional")

    def _get_professional(self):
        for session in self:
            session.professional = session.treatment.professional