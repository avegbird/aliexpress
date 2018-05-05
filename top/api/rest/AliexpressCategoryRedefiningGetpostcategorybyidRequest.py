'''
Created by auto_sdk on 2018.04.18
'''
from top.api.base import RestApi
class AliexpressCategoryRedefiningGetpostcategorybyidRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param0 = None

	def getapiname(self):
		return 'aliexpress.category.redefining.getpostcategorybyid'
