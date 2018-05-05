'''
Created by auto_sdk on 2018.03.07
'''
from top.api.base import RestApi
class AliexpressMerchantRedefiningQueryremarkRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_type = None
		self.remark_id = None

	def getapiname(self):
		return 'aliexpress.merchant.redefining.queryremark'
