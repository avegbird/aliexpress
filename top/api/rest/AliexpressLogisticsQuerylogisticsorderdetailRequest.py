'''
Created by auto_sdk on 2018.01.11
'''
from top.api.base import RestApi
class AliexpressLogisticsQuerylogisticsorderdetailRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.current_page = None
		self.domestic_logistics_num = None
		self.gmt_create_end_str = None
		self.gmt_create_start_str = None
		self.international_logistics_num = None
		self.logistics_status = None
		self.page_size = None
		self.trade_order_id = None
		self.warehouse_carrier_service = None

	def getapiname(self):
		return 'aliexpress.logistics.querylogisticsorderdetail'
