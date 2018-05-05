'''
Created by auto_sdk on 2017.12.06
'''
from top.api.base import RestApi
class AliexpressDataRedefiningQueryproductbusinessinfobyidRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param_string = None

	def getapiname(self):
		return 'aliexpress.data.redefining.queryproductbusinessinfobyid'
