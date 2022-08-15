from odoo import models, fields, api


class SaleMoveHeritfacturee(models.Model):
    _inherit = 'sale.order'
    sale_date_Facture = fields.Date("Date de prochaine facturation")
    sale_park = fields.Boolean(default=False)
    sale_periode = fields.Integer(default='0')
    sale_test1 = fields.Integer(default='0')
    sale_test2 = fields.Integer(default='0')
    sale_test3 = fields.Integer(default='0')


    #bon de commande automatique

    sale_date_bon_de_commande = fields.Date("Date de prochaine bon de commande")
    sale_not_update_bon_commande = fields.Boolean(default=False, string='non à jour')
    sale_date_de_fin_contrat = fields.Date("Date de fin de contart")
class AcountMoveHeritFIN(models.Model):
    _inherit = 'account.move'
    acount_maintnance = fields.Boolean(string="Maintenance", default=False)
