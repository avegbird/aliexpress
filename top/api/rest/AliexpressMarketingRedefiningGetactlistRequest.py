'''
Created by auto_sdk on 2017.12.28
'''
from top.api.base import RestApi
class AliexpressMarketingRedefiningGetactlistRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param_seller_coupon_activity_api_query = None

	def getapiname(self):
		return 'aliexpress.marketing.redefining.getactlist'
