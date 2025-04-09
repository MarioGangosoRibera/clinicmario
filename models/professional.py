from odoo import models, fields, api


class Professional(models.Model):
    _name= "clinicmario.professional"
    _description = "clinicmario.professional"

    id = fields.Integer()
    name = fields.Char(required = True, string="Nombre")
    surnames = fields.Char(required = True, string="Apellidos")
    proftype = fields.Selection(string="Tipo", selection=[('muscular', 'Muscular'), ('deportivo', 'Deportivo'), ('geriatrico', 'Geriátrico'), ('pediatrico', 'Pediátrico')], default='muscular')
    phone = fields.Integer(string="Nº de Teléfono")
    email = fields.Text(string="Correo Electrónico")

    # Un profesional puede desarrollar varios tratamientos y un tratamiento está a cargo de un único profesional
    treatments = fields.One2many(string="Tratamientos", comodel_name="clinicmario.treatment", inverse_name="professional")

    sessions = fields.One2many("clinicmario.session",compute="_compute_sessions", string="Sesiones")

    def _compute_sessions(self):
        for professional in self:
            sessions=self.env["clinicmario.session"].search([("treatment.professional","=",professional.id)])
            professional.sessions=sessions
