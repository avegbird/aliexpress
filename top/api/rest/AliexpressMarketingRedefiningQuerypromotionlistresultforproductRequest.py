'''
Created by auto_sdk on 2018.01.29
'''
from top.api.base import RestApi
class AliexpressMarketingRedefiningQuerypromotionlistresultforproductRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.prom_product_single_query_d_t_o = None

	def getapiname(self):
		return 'aliexpress.marketing.redefining.querypromotionlistresultforproduct'
