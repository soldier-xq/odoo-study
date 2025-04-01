from email.policy import default

from odoo import models, fields, api
from datetime import timedelta


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = '房产报价'
    _order = 'price desc'

    price = fields.Float(string="价格")
    status = fields.Selection(string="报价状态",selection=[('accepted', '接受'), ('refused', '拒绝')],copy=False)
    partner_id = fields.Many2one('res.partner',string="客户",required=True)
    property_id = fields.Many2one('estate.property',string="房产",required=True)
    validity = fields.Integer(string="有效期",default=7)
    date_deadline = fields.Date(string="截止日期",compute="_compute_date_deadline",inverse="_inverse_date_deadline")

    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', '报价必须为正数'),
    ]

    @api.depends('create_date','validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days

    def action_accept(self):
        for record in self:
            record.status = 'accepted'
            # record.partner_id.action_refuse()
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id.id

    def action_refuse(self):
        for record in self:
            record.status = 'refused'