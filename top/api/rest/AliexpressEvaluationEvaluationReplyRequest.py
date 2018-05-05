'''
Created by auto_sdk on 2018.03.30
'''
from top.api.base import RestApi
class AliexpressEvaluationEvaluationReplyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.child_order_id = None
		self.parent_order_id = None
		self.text = None

	def getapiname(self):
		return 'aliexpress.evaluation.evaluation.reply'
