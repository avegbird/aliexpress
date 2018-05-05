'''
Created by auto_sdk on 2018.03.19
'''
from top.api.base import RestApi
class AliexpressProductProductgroupsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'aliexpress.product.productgroups.get'
