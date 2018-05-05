'''
Created by auto_sdk on 2017.12.29
'''
from top.api.base import RestApi
class AliexpressOfferRedefiningCopysizetemplateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.size_template_id = None
		self.target_leaf_id = None

	def getapiname(self):
		return 'aliexpress.offer.redefining.copysizetemplate'
