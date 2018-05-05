'''
Created by auto_sdk on 2017.08.14
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningEditsingleskupriceRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.product_id = None
		self.sku_id = None
		self.sku_price = None

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.editsingleskuprice'
