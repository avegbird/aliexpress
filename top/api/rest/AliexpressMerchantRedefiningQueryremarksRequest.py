'''
Created by auto_sdk on 2018.03.15
'''
from top.api.base import RestApi
class AliexpressMerchantRedefiningQueryremarksRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_type = None
		self.remark_ids = None

	def getapiname(self):
		return 'aliexpress.merchant.redefining.queryremarks'
