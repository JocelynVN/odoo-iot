import base64

from odoo import models, fields, api, _
from odoo.tools import file_open


class IoTBox(models.Model):
    _name = 'iot.box'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = 'IoT Box'
    _check_company_auto = True

    def _default_image(self):
        with file_open('iot_box/static/img/iot-box.png', 'rb') as file:
            return base64.b64encode(file.read())

    name = fields.Char(string='Name', translate=True, tracking=True)
    state = fields.Selection(
        [('connected', 'Connected'), ('disconnected', 'Disconnected')], default='disconnected',
        string='Connection Status', help="Connection status of IoT Box & Server.", tracking=True
    )
    ip = fields.Char(string='IP Address', help="IP Address of the IoT Box.", tracking=True)
    identifier_code = fields.Char(string='Identifier Code', tracking=True, help="Identifier code of the IoT Box, each IoT Box will be assigned a unique identifier code.")
    token = fields.Char(string='Token', tracking=True)
    company_id = fields.Many2one('res.company', string='Company', tracking=True, domain=lambda self: [('id', 'in', self.env.user.company_ids.ids)])
    device_ids = fields.One2many('iot.device', 'iot_box_id', string='Control Devices')
    device_nb = fields.Integer(
        string='Number Of Control Devices', compute='_compute_device_nb',
        help="The number of devices that the IoT box has connected and controlled"
    )
    image_1920 = fields.Image(default=_default_image)

    _sql_constraints = [('identifier_code_uniq', "unique(identifier_code)", "The identifier code of the iot box must be unique.")]

    @api.depends('device_ids')
    def _compute_device_nb(self):
        grouped_data = self.env['iot.device']._read_group([('iot_box_id', 'in', self.ids)], ['iot_box_id'], ['__count'])
        mapped_data = {item.id: count for item, count in grouped_data}
        for r in self:
            r.device_nb = mapped_data.get(r.id, 0)

    def action_connection(self):
        self.state = 'connected'
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'success',
                'message': _("Connected successfully!"),
                'next': {'type': 'ir.actions.act_window_close'}
            }
        }

    def action_open_devices(self):
        devices = self.device_ids
        action = self.env['ir.actions.act_window']._for_xml_id('iot_box.iot_device_act')
        if len(devices) != 1:
            action['domain'] = [('id', 'in', devices.ids)]
        else:
            res = self.env.ref('iot_box.iot_device_form_view', False)
            action['views'] = [(res and res.id or False, 'form')]
            action['res_id'] = devices.id
        action['context'] = {'search_default_grp_type': 1}
        return action
