from odoo import fields, models, api


class InheritSaleOrder(models.Model):
    _inherit = 'project.task'

    sale_order_ids = fields.One2many('sale.order', 'task', string='Sale Order')


    def sale_order_task(self):
        pass
