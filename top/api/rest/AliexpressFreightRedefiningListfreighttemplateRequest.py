'''
Created by auto_sdk on 2017.08.14
'''
from top.api.base import RestApi
class AliexpressFreightRedefiningListfreighttemplateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'aliexpress.freight.redefining.listfreighttemplate'
