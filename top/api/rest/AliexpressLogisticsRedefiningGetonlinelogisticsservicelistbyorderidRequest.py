'''
Created by auto_sdk on 2018.01.10
'''
from top.api.base import RestApi
class AliexpressLogisticsRedefiningGetonlinelogisticsservicelistbyorderidRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.goods_height = None
		self.goods_length = None
		self.goods_weight = None
		self.goods_width = None
		self.order_id = None

	def getapiname(self):
		return 'aliexpress.logistics.redefining.getonlinelogisticsservicelistbyorderid'
