'''
Created by auto_sdk on 2017.12.27
'''
from top.api.base import RestApi
class AliexpressMarketingRedefiningAdjustlimiteddiscountpromendtimebetaRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.prom_id = None
		self.promotion_end_time = None

	def getapiname(self):
		return 'aliexpress.marketing.redefining.adjustlimiteddiscountpromendtimebeta'
