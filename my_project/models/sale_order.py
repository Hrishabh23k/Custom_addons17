from odoo import fields, models, api


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    task = fields.Many2one('project.task', string='Task')
    sale_order_wizard = fields.Many2many('sale.order.wizard', 'sale_wizard', 'sow', 'so', string='SaleWizard')
    custom_order_sale = fields.One2many('custom.sale.order', 'so', string="CustomOrderSale")

    def remove_task(self):
        self.task = False

class CustomSaleOrder(models.Model):
    _name = 'custom.sale.order'

    so = fields.Many2one('sale.order', string="SaleOrder")
    name = fields.Char(string="Name")
    total = fields.Float(string="Total")
