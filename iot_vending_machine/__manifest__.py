{
    'name': "IoT & Vending Machines",
    'name_vi_VN': "IoT & Máy bán hàng tự động",
    'summary': """
Connect and collect information about IoT Box with vending machine.
    """,

    'summary_vi_VN': """
Kết nối và thu thập các thông tin giữa hộp IoT với máy bán hàng tự động.
    """,

    'description': """

What it does
============
This module acts as a bridge to manage the connection of vending machine to the IoT box through the Odoo application.

Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô-đun này làm gì?
==================
Mô-đun này đóng vai trò là cầu nối để quản lý kết nối máy bán hàng tự động với hộp IoT thông qua ứng dụng Odoo.

Ấn bản được hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Jocelyn",
    'category': 'Internet of Things (IoT)',
    'version': '0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['iot_box'],

    # always loaded
    'data': [],
    
    'installable': True,
    'price': 99.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
