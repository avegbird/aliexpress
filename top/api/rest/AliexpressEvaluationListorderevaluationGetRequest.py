'''
Created by auto_sdk on 2018.03.30
'''
from top.api.base import RestApi
class AliexpressEvaluationListorderevaluationGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.trade_evaluation_request = None

	def getapiname(self):
		return 'aliexpress.evaluation.listorderevaluation.get'
