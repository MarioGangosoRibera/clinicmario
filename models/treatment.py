from odoo import models, fields, api


class Treatment(models.Model):
    _name= "clinicmario.treatment"
    _description = "clinicmario.treatment"

    id = fields.Integer()
    name = fields.Char(required = True, string="Nombre", compute = "_get_name")
    description = fields.Text(string="Descripción")
    initdate = fields.Datetime(string="Fecha de Inicio")
    enddate = fields.Datetime(string="Fecha de Fin")

    # Un registro puede tener varios tratamientos y un tratamiento tiene un solo registro
    register = fields.Many2one("clinicmario.register", ondelete = "CASCADE", string="Registro")

    # Un tratamiento puede tener varias sesiones y cada sesión tiene un único tratamiento
    sessions = fields.One2many(comodel_name="clinicmario.session", inverse_name = "treatment", readonly = True, string="Sesiones")

    # Un profesional puede desarrollar varios tratamientos y un tratamiento está a cargo de un único profesional
    professional = fields.Many2one("clinicmario.professional", ondelete = "CASCADE", string="Profesional")

    @api.depends("register") # Cuando se actualice el registro, se rellena el campo
    def _get_name(self): 
        for treatment in self: # Se recorren los tratamientos
            if treatment.register: # Si se ha introducido un registro:
                treatment.name = f"{treatment.register.client.name} - {treatment.register.name}" 
            else: # Si no se ha introducido ningún registro, se borra el nombre (Para que no de errores raros)
                treatment.name = False