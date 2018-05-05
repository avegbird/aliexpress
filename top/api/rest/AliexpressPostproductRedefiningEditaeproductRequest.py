'''
Created by auto_sdk on 2018.04.02
'''
from top.api.base import RestApi
class AliexpressPostproductRedefiningEditaeproductRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.aeop_a_e_product = None

	def getapiname(self):
		return 'aliexpress.postproduct.redefining.editaeproduct'
