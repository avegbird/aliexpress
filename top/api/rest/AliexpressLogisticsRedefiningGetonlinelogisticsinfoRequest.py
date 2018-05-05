'''
Created by auto_sdk on 2017.08.14
'''
from top.api.base import RestApi
class AliexpressLogisticsRedefiningGetonlinelogisticsinfoRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.china_logistics_id = None
		self.current_page = None
		self.gmt_create_end_str = None
		self.gmt_create_start_str = None
		self.international_logistics_id = None
		self.logistics_status = None
		self.order_id = None
		self.page_size = None
		self.query_express_order = None

	def getapiname(self):
		return 'aliexpress.logistics.redefining.getonlinelogisticsinfo'
