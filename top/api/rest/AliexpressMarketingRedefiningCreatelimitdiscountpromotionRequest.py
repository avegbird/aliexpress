'''
Created by auto_sdk on 2017.12.27
'''
from top.api.base import RestApi
class AliexpressMarketingRedefiningCreatelimitdiscountpromotionRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.store_promotion = None

	def getapiname(self):
		return 'aliexpress.marketing.redefining.createlimitdiscountpromotion'
