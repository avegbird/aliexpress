'''
Created by auto_sdk on 2018.03.15
'''
from top.api.base import RestApi
class AliexpressOfferRedefiningInitialnewbundleRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.main_item_id = None
		self.sub_item_list = None

	def getapiname(self):
		return 'aliexpress.offer.redefining.initialnewbundle'
