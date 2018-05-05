'''
Created by auto_sdk on 2017.08.14
'''
from top.api.base import RestApi
class AliexpressLogisticsSellermodifiedshipmentfortopRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.description = None
		self.new_logistics_no = None
		self.new_service_name = None
		self.old_logistics_no = None
		self.old_service_name = None
		self.out_ref = None
		self.send_type = None
		self.tracking_website = None

	def getapiname(self):
		return 'aliexpress.logistics.sellermodifiedshipmentfortop'
