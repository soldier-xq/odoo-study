from email.policy import default

from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = '房产类型'

    name = fields.Char(string="房产类型",required=True)
