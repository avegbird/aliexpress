'''
Created by auto_sdk on 2018.03.26
'''
from top.api.base import RestApi
class AliexpressCategoryRedefiningGetchildattributesresultbypostcateidandpathRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param1 = None
		self.param2 = None

	def getapiname(self):
		return 'aliexpress.category.redefining.getchildattributesresultbypostcateidandpath'
