{
    'name': "Internet Of Things",
    'name_vi_VN': "Internet Of Things",
    'summary': """
Connect and collect information about IoT Box and peripheral devices.
    """,

    'summary_vi_VN': """
Kết nối và thu thập các thông tin về hộp IoT và các thiết bị ngoại vi.
    """,

    'description': """

What it does
============

Desire to connect peripheral devices with Odoo.

Editions Supported
==================

This module serves as a bridge to connect peripheral devices with Odoo through an IoT Box,

1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Vấn đề
======

Mong muốn kết nối các thiết bị ngoại vi với odoo.

Giải pháp
=========

Module này là cầu nối giúp kết nối các thiết bị ngoại vi với odoo thông qua hộp IoT Box.

Ấn bản được hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Jocelyn",
    'category': 'Internet of Things (IoT)',
    'version': '0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/root_menu.xml",
        "views/iot_box_views.xml",
        "views/iot_device_views.xml",
    ],
    'images': ['static/description/icon.png'],
    
    'installable': True,
    'application': True,
    'price': 99.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
