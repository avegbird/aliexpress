'''
Created by auto_sdk on 2017.08.14
'''
from top.api.base import RestApi
class AliexpressLogisticsRedefiningGetprintinfoRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.international_logistics_id = None

	def getapiname(self):
		return 'aliexpress.logistics.redefining.getprintinfo'
