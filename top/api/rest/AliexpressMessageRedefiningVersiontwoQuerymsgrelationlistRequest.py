'''
Created by auto_sdk on 2018.04.03
'''
from top.api.base import RestApi
class AliexpressMessageRedefiningVersiontwoQuerymsgrelationlistRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.query = None

	def getapiname(self):
		return 'aliexpress.message.redefining.versiontwo.querymsgrelationlist'
