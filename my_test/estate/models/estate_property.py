from email.policy import default

from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string="名称",required=True)
    description = fields.Text(string="描述")
    postcode = fields.Char(string="邮编")
    date_availability = fields.Date(string="可用日期",default=fields.Date.today())
    expected_price = fields.Float(string="期望售价",required=True)
    selling_price = fields.Float(string="售价",readonly=True)
    bedrooms = fields.Integer(string="卧室",default=2)
    living_area = fields.Integer(string="客厅面积")
    facades = fields.Integer(string="门数")
    garage = fields.Boolean(string="车库")
    garden = fields.Boolean(string="花园")
    garden_area = fields.Integer(string="花园面积")
    garden_orientation = fields.Selection(
        string="花园方向",
        selection=[('north', '北'), ('south', '南'), ('east', '东'), ('west', '西')]
    )
    active = fields.Boolean(string="是否归档",default=True)
    state = fields.Selection(string="状态",selection=[('new', '新建'), ('offer_received', '报价接收'), ('offer_accepted', '报价接受'), ('sold', '已售'), ('canceled', '已取消')],default='new')
    property_typ_id = fields.Many2one('estate.property.type',string="房产类型")
    buyer_id = fields.Many2one('res.partner',string="买家",copy=False)
    seller_id = fields.Many2one('res.users',string="卖家",default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag',string="标签")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="报价")
    total_area = fields.Float(string="总面积",compute="_compute_total_area",store=True)
    best_price = fields.Float(string="最佳报价",compute="_compute_best_price",store=True)

    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price')) if record.offer_ids else 0.0