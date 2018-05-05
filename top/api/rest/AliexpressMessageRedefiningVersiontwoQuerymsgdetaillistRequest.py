'''
Created by auto_sdk on 2018.04.03
'''
from top.api.base import RestApi
class AliexpressMessageRedefiningVersiontwoQuerymsgdetaillistRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.channel_id = None
		self.current_page = None
		self.extern_id = None
		self.page_size = None

	def getapiname(self):
		return 'aliexpress.message.redefining.versiontwo.querymsgdetaillist'
