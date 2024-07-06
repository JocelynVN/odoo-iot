import base64

from odoo import api, models, fields
from odoo.tools import file_open


class IoTDevice(models.Model):
    _name = 'iot.device'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = 'IoT Device'

    def _default_image(self):
        with file_open('iot_box/static/img/device.png', 'rb') as file:
            return base64.b64encode(file.read())

    name = fields.Char(string='Name', required=True, translate=True, tracking=True)
    company_id = fields.Many2one(related='iot_box_id.company_id')
    state = fields.Selection(
        [('connected', 'Connected'), ('disconnected', 'Disconnected')], default="disconnected",
        string='Connection Status', help="Connection status of IoT Box & Device.", tracking=True
    )
    identifier_code = fields.Char(
        string='Identifier Code', tracking=True,
        help="Identifier code of the device, each device will be assigned a unique identifier code."
    )
    iot_box_id = fields.Many2one('iot.box', string='IoT Box', required=True, ondelete='cascade', tracking=True)
    brand = fields.Char(string='Brand')
    type = fields.Selection([], string='Type', required=True, help="Type of device connected to the IoT box.")
    image_1920 = fields.Image(default=_default_image)

    _sql_constraints = [('identifier_code_uniq', "unique(identifier_code)", "The identifier code of the iot device must be unique.")]

    @api.onchange('type')
    def _onchange_device_type(self):
        pass
