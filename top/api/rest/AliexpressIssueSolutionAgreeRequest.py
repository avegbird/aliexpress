'''
Created by auto_sdk on 2018.04.17
'''
from top.api.base import RestApi
class AliexpressIssueSolutionAgreeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_login_id = None
		self.issue_id = None
		self.return_address_id = None
		self.solution_id = None

	def getapiname(self):
		return 'aliexpress.issue.solution.agree'
