from odoo import api, fields, models


class ProductCost(models.Model):
    _inherit = "sale.order"

    hide_cost = fields.Boolean(string="Cost Should Be Hidden", compute="_check_user_cost_privilege")

    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            record.hide_cost = self.env.user.has_group("hide_cost.group_see_cost_user")