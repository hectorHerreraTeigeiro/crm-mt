# -*- coding: utf-8 -*-
from odoo import fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Add a new column to the crm.lead model, in order to save the sale progress status
    # Changes requested by Sales Direction
    prosp_basedatos = fields.Char(string="Base de datos", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    prosp_evento = fields.Char(string="Evento", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    prosp_ae_id = fields.Many2one(comodel_name="res.partner", string="Account Executive", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    prosp_cteref_id = fields.Many2one(comodel_name="res.partner", string="Cliente referencia", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    prosp_callctr = fields.Char(string="Call center", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    prosp_otro = fields.Char(string="Otro", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    prosp_comment = fields.Char(string="Comentarios", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    calif_tienepry = fields.Boolean(string="Tiene proyecto", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    calif_tieneppto = fields.Boolean(string="Tiene presupuesto", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    calif_plazo = fields.Integer(string="Plazo", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    calif_compralocal = fields.Boolean(string="Compra local", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    calif_decidelocal = fields.Boolean(string="Decide local", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    calif_primerprov = fields.Boolean(string="Primer proveedor", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    calif_regfabricante = fields.Boolean(string="Registro fabricante", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    calif_comment = fields.Char(string="Comentarios", required=False, )
    inv_radiografia = fields.Boolean(string="Radiografia cuenta", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    inv_equipotrabajo = fields.Boolean(string="Equipo trabajo", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    inv_alcance = fields.Boolean(string="Alcance", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    inv_ingenieria = fields.Boolean(string="Ingenieria", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    inv_competencia = fields.Char(string="Competencia", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    inv_apoyofabric = fields.Char(string="Apoyo fabricantes", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    inv_mapacontactos = fields.Boolean(string="Mapa contactos", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    inv_comment = fields.Char(string="Comentarios", required=False, )
    pres_margenutil = fields.Integer(string="Margen utilidad", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    pres_descfabric = fields.Boolean(string="Desc fabricante aplicados", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    pres_revising = fields.Boolean(string="Revision ingenieria", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    pres_vobointerno = fields.Boolean(string="Vobo interno", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    pres_contactoenvio_id = fields.Many2one(comodel_name="res.partner", string="Contacto envio prop", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    pres_fechalimprop = fields.Date(string="Fecha lim entrega prop", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    pres_recepconfirm = fields.Date(string="Recep y conf prop cliente", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    pres_propganadora = fields.Boolean(string="Propuesta ganadora", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    pres_comment = fields.Char(string="Comentarios", required=False, )
    cie_revpropclte = fields.Boolean(string="Revis prop con cliente", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    cie_manejoobjec = fields.Boolean(string="Manejo objecc", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    cie_cierreverbal = fields.Date(string="Cierre verbal", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    cie_conffecharecepPO = fields.Date(string="Confir fecha recep PO", required=False,
                                   help="Estimate of the date on which the opportunity will be won.", )
    cie_comment = fields.Char(string="Comentarios", required=False, )
