'''
Created by auto_sdk on 2018.01.29
'''
from top.api.base import RestApi
class AliexpressWarrantyOrderQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.warranty_id = None

	def getapiname(self):
		return 'aliexpress.warranty.order.query'
