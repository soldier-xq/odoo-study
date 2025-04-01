from email.policy import default

from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = '房产标签'
    _order = 'name desc'

    name = fields.Char(string="房产标签",required=True)
    color = fields.Integer(string="颜色",default=10)

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', '标签名称必须唯一'),
    ]
