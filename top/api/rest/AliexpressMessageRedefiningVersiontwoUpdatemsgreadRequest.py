'''
Created by auto_sdk on 2018.01.25
'''
from top.api.base import RestApi
class AliexpressMessageRedefiningVersiontwoUpdatemsgreadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.channel_id = None

	def getapiname(self):
		return 'aliexpress.message.redefining.versiontwo.updatemsgread'
