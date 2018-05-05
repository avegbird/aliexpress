# -*- coding: utf-8 -*-
import urllib2
import json


class DingHolder(object):
    def __init__(self):
        self.token_url = "https://oapi.dingtalk.com/sns/gettoken"
        self.tmp_url = "https://oapi.dingtalk.com/sns/get_persistent_code"
        self.sns_url = "https://oapi.dingtalk.com/sns/get_sns_token"
        self.user_url = "https://oapi.dingtalk.com/sns/getuserinfo"
        self.user_id = "https://oapi.dingtalk.com/user/getUseridByUnionid"
        self.crop_token = "https://oapi.dingtalk.com/gettoken"
        self.user_info = "https://oapi.dingtalk.com/user/get"
        self.js_api = "https://oapi.dingtalk.com/get_jsapi_ticket"
        self.user_id_bytoken = "https://oapi.dingtalk.com/user/getuserinfo"
        self.signature_url = "https://debug.dingtalk.com/apiagent/createSignature"

    def _get_access_token(self):
        """
            get access_token
        :return: access_token
        """
        url = self.token_url
        url = url + '?' + 'appid=' + self.appid + '&appsecret=' + self.appsecret
        return_data = self._do_get(url)
        if return_data['errcode'] == 40001:
            return {"errcode": "err", "errmsg": return_data["errmsg"]}
        return {"errcode": "ok", "errmsg": return_data['access_token']}

    def _get_persistent_code(self, access_token, crop_token, tmpcode):
        """
            get persistent_code
        :param access_token:
        :param tmpcode:
        :return: None
        """
        param = json.dumps({"tmp_auth_code": tmpcode})
        url = self.tmp_url + "?access_token=" + access_token
        data = self._do_post(url, param)
        if data['errcode'] == 40078:
            return {"errcode": "err", "errmsg": "错误的请求操作，请重试。"}
        unionid = data['unionid']
        user_data = self._get_userId(crop_token, unionid)
        if user_data['errcode'] == 'err':
            return {"errcode": "err", "errmsg": user_data['errmsg']}
        elif user_data['errcode'] == 'ok':
            return {"errcode": "ok", "errmsg": user_data['errmsg']}

    def _get_sns_token(self, access_token, persistent_token, openid):
        """
            get sns_token
        :param access_token:
        :param persistent_token:
        :param openid:
        :return: none
        """
        sns_data = json.dumps({"persistent_code": persistent_token, "openid": openid})
        requrl = self.sns_url + "?access_token=" + access_token
        headers = {'Content-Type': 'application/json'}
        req = urllib2.Request(url=requrl, data=sns_data, headers=headers)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        persistent_datas = json.loads(res)
        sns_token = persistent_datas['sns_token']
        return self._get_user_info(access_token, sns_token)

    def _get_user_info(self, access_token, sns_token):
        """
            get simple userInfo
        :param access_token:
        :param sns_token:
        :return: none
        """
        requrl = self.user_url + "?sns_token=" + sns_token
        res_data = urllib2.urlopen(requrl)
        json_data = json.loads(res_data.read())
        unionid = json_data['user_info']['unionid']
        return self._get_userId(access_token, unionid)

    def _get_userId(self, crop_token, unionid):
        """
            get_userId
        :param crop_token:
        :param unionid:
        :return: none
        :errcode：60121
        """
        url = self.user_id + "?access_token=" + crop_token + "&unionid=" + unionid
        json_data = self._do_get(url)
        if json_data['errcode'] == 60121:
            return {"errcode": "err", "errmsg": "您还未加入该公司或团队，暂时没有权限登录。"}
        userid = json_data['userid']
        return {"errcode": "ok", "errmsg": self._get_user(crop_token, userid)}

    def _get_jsapi_ticket(self, access_token):
        url = self.js_api + "?access_token=" + access_token
        json_data = self._do_get(url)
        if json_data['errcode'] == 45009:
            return {"errcode": "err", "errmsg": json_data["errmsg"]}
        return {"errcode": "ok", "errmsg": json_data['ticket']}

    def _get_user(self, crop_token, userid):
        url = self.user_info + "?access_token=" + crop_token + "&userid=" + userid
        json_data = self._do_get(url)
        return json_data

    def _do_get(self, url):
        res_data = urllib2.urlopen(url)
        json_data = json.loads(res_data.read())
        return json_data

    def _do_post(self, url, param):
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        req = urllib2.Request(url=url, data=param, headers=headers)
        res_data = urllib2.urlopen(req)
        json_data = json.loads(res_data.read())
        return json_data

    def _get_parameters(self, param):
        return_data = ''
        for k, v in param:
            return_data += k + '=' + v + '&'
        return return_data[:-1]


dp = DingHolder()