'''
Created by auto_sdk on 2018.03.16
'''
from top.api.base import RestApi
class AliexpressMarketingRedefiningUpdatelimiteddiscountpromotionRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.limited_discount_prom_product_d_t_o = None

	def getapiname(self):
		return 'aliexpress.marketing.redefining.updatelimiteddiscountpromotion'
