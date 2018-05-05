'''
Created by auto_sdk on 2018.04.16
'''
from top.api.base import RestApi
class AliexpressIssueImageUploadRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.buyer_login_id = None
		self.extension = None
		self.image_bytes = None
		self.issue_id = None

	def getapiname(self):
		return 'aliexpress.issue.image.upload'

	def getMultipartParas(self):
		return ['image_bytes']
