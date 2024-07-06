from odoo import models, fields


class IoTDevice(models.Model):
    _name = 'iot.device'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'IoT Device'

    name = fields.Char(string='Name', readonly=True, translate=True)
    company_id = fields.Many2one(related='iot_box_id.company_id')
    state = fields.Selection(
        [('connected', 'Connected'), ('disconnected', 'Disconnected')],
        string='Connection Status', help="Connection status of IoT Box & Device.", tracking=True
    )
    identifier = fields.Char(
        string='Identifier', readonly=True, tracking=True,
        help="Identifier of the device, each device will be assigned a unique identifier."
    )
    iot_box_id = fields.Many2one('iot.box', string='IoT Box', required=True, ondelete='cascade', tracking=True)
    brand = fields.Char(string='Brand')
    type = fields.Selection([('vending_machine', 'Vending Machine')], string='Type', readonly=True, help="Type of device connected to the IoT box.")
