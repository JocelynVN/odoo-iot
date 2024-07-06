{
    'name': "Internet Of Things (IoT)",
    'name_vi_VN': "Internet Of Things (IoT)",
    'summary': """
Manage connect and collect information between IoT Box with peripheral devices.
    """,

    'summary_vi_VN': """
Quản lý kết nối và thu thập các thông tin giữa hộp IoT với các thiết bị ngoại vi.
    """,

    'description': """

What it does?
=============
This module acts as a bridge to manage the connection of peripheral devices to the IoT box through the Odoo application.

Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô-đun này làm gì?
==================
Mô-đun này đóng vai trò là cầu nối để quản lý việc kết nối các thiết bị ngoại vi với hộp IoT thông qua ứng dụng Odoo.

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
