'''
Created by auto_sdk on 2017.11.17
'''
from top.api.base import RestApi
class AliexpressMerchantRedefiningQueryservicescoreinfoRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param1 = None
		self.param2 = None

	def getapiname(self):
		return 'aliexpress.merchant.redefining.queryservicescoreinfo'
