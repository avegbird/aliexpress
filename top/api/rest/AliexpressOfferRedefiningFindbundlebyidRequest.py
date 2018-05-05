'''
Created by auto_sdk on 2017.11.28
'''
from top.api.base import RestApi
class AliexpressOfferRedefiningFindbundlebyidRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.bundle_id = None

	def getapiname(self):
		return 'aliexpress.offer.redefining.findbundlebyid'
