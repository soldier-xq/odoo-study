from email.policy import default

from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = '房产类型'
    _order = 'sequence desc'

    name = fields.Char(string="房产类型",required=True)
    property_ids = fields.One2many('estate.property','property_typ_id',string="房产")
    sequence = fields.Integer(string="顺序",default=10)

    _sql_constraints = [('name_unique','unique(name)',"房屋签名必须唯一")]