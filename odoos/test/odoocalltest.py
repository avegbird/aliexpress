# -*- coding: utf-8 -*-
from odoos.tools.OdooCall import OdooCall

oc = OdooCall(1, "Rhyx1919", "prod_herp_v1")
print oc._call_odoo('logistics.record', "get_logistics_company", "顺")