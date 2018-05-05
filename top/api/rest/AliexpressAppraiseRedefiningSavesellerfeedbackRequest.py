'''
Created by auto_sdk on 2018.01.23
'''
from top.api.base import RestApi
class AliexpressAppraiseRedefiningSavesellerfeedbackRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param1 = None

	def getapiname(self):
		return 'aliexpress.appraise.redefining.savesellerfeedback'
