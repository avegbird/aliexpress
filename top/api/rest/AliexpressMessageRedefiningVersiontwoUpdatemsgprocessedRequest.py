'''
Created by auto_sdk on 2018.03.21
'''
from top.api.base import RestApi
class AliexpressMessageRedefiningVersiontwoUpdatemsgprocessedRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.channel_id = None
		self.deal_stat = None

	def getapiname(self):
		return 'aliexpress.message.redefining.versiontwo.updatemsgprocessed'
