'''
Created by auto_sdk on 2018.04.10
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningFindaeproductbyidRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.product_id = None

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.findaeproductbyid'
