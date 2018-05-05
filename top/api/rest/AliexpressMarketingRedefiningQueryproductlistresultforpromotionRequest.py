'''
Created by auto_sdk on 2018.01.02
'''
from top.api.base import RestApi
class AliexpressMarketingRedefiningQueryproductlistresultforpromotionRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.promotion_id = None

	def getapiname(self):
		return 'aliexpress.marketing.redefining.queryproductlistresultforpromotion'
