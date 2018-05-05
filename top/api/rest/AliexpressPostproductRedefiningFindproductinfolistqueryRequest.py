'''
Created by auto_sdk on 2018.03.14
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningFindproductinfolistqueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.aeop_a_e_product_list_query = None

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.findproductinfolistquery'
