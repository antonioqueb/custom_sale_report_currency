# __manifest__.py
{
    'name': 'Custom Sale Report Currency',
    'version': '1.0',
    'summary': 'Add currency symbol (MXN or USD) to sale order report',
    'author': 'Alphaqueb Consulting',
    'category': 'Sales',
    'depends': ['sale_management'],
    'data': ['views/sale_report_template.xml'],
    'installable': True,
    'application': False,
}
