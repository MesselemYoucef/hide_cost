from odoo import api, fields, models


class ProductCostHide(models.Model):
    _inherit = "product.template"

    hide_cost = fields.Boolean(string="Cost Should Be Hidden", compute="_check_user_cost_privilege")

    @api.depends("name")
    def _check_user_cost_privilege(self):
        for record in self:
            self.hide_cost = self.env.user.has_group("hide_cost.group_see_cost_user")
