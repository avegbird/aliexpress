'''
Created by auto_sdk on 2017.08.14
'''
from top.api.base import RestApi
class AliexpressPhotobankRedefiningUploadimageRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.file_name = None
		self.group_id = None
		self.image_bytes = None

	def getapiname(self):
		return 'aliexpress.photobank.redefining.uploadimage'

	def getMultipartParas(self):
		return ['image_bytes']
