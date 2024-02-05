from odoo import fields, models, api


class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'

    sale_order_ids = fields.Many2many('sale.order', 'sale_wizard', 'so', 'sow', string='SaleOrder')

    def save_object(self):
        active_id = self.env.context.get('active_id')
        pro = self.env['project.task'].browse(active_id)
        for rec in self.sale_order_ids:
            pro.write({
                'sale_order_ids': [(4, rec.id)],
            })
            print(rec.id, rec.name, rec.amount_total)
        print(pro.id, pro)


