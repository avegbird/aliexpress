'''
Created by auto_sdk on 2018.02.07
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningEditmultilanguageproductRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.aeop_a_e_product_multilanguage_info = None
		self.product_id = None

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.editmultilanguageproduct'
