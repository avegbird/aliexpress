'''
Created by auto_sdk on 2017.12.08
'''
from top.api.base import RestApi
class AliexpressDataRedefiningQueryproductfavoritedinfoeverydaybyidRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.current_page = None
		self.end_date = None
		self.page_size = None
		self.product_id = None
		self.start_date = None

	def getapiname(self):
		return 'aliexpress.data.redefining.queryproductfavoritedinfoeverydaybyid'
