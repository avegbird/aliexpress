'''
Created by auto_sdk on 2017.08.14
'''
from top.api.base import RestApi
class AliexpressLogisticsRedefiningGetlogisticsselleraddressesRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.seller_address_query = None

	def getapiname(self):
		return 'aliexpress.logistics.redefining.getlogisticsselleraddresses'
