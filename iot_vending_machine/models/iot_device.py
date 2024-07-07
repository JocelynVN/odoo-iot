import base64

from odoo import api, models, fields
from odoo.tools import file_open


class IoTDevice(models.Model):
    _inherit = 'iot.device'

    type = fields.Selection(selection_add=[('vending_machine', 'Vending Machine')], ondelete={'vending_machine': 'cascade'})

    @api.onchange('type')
    def _onchange_device_type(self):
        super(IoTDevice, self)._onchange_device_type()
        if self.type == 'vending_machine':
            with file_open('iot_vending_machine/static/img/vending-machine.png', 'rb') as file:
                self.image_1920 = base64.b64encode(file.read())
