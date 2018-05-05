'''
Created by auto_sdk on 2017.08.14
'''
from top.api.base import RestApi
class AliexpressFreightRedefiningCalculatefreightRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.country = None
		self.freight_template_id = None
		self.height = None
		self.is_custom_pack_weight = None
		self.length = None
		self.pack_add_unit = None
		self.pack_add_weight = None
		self.pack_base_unit = None
		self.product_price = None
		self.weight = None
		self.width = None

	def getapiname(self):
		return 'aliexpress.freight.redefining.calculatefreight'
