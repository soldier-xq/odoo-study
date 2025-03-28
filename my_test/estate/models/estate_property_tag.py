from email.policy import default

from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = '房产标签'

    name = fields.Char(string="房产标签",required=True)
