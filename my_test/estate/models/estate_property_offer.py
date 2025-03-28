from email.policy import default

from odoo import models, fields


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = '房产报价'

    price = fields.Float(string="价格")
    status = fields.Selection(string="报价状态",selection=[('accepted', '接受'), ('refused', '拒绝')],copy=False)
    partner_id = fields.Many2one('res.partner',string="客户",required=True)
    property_id = fields.Many2one('estate.property',string="房产",required=True)
