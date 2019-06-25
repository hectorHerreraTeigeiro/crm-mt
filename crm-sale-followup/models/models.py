# -*- coding: utf-8 -*-
"""Adding fields for Sales tracking in the Opportunity """

from odoo import models, fields, api

class CrmLead(models.Model):


    _name = "crm.lead"
    _inherit = [_name, "crm-sale-followup.info"]

    s01 = fields.Char(string="String de s01", required=False, )
    s02 = fields.Char(string="String de s02", required=False, )
    s03 = fields.Char(string="String de s03", required=False, )
    s04 = fields.Char(string="String de s04", required=False, )

