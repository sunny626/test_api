# _*_coding:utf-8 _*_
# @Time     :2018/12/30 22:18
# @Author   :sunny
# @Email    :602992114@qq.com

import requests
import json
from api_test_sunny.common.config import ConfigLoader

class Requests:

    def __init__(self,method,url,param=None,cookies=None,headers=None):
        try:
            conf=ConfigLoader()
            url_pre=conf.get("api","url_pre")
            url=url_pre+url
            if method=="get":
                self.res=requests.get(url=url,params=param,cookies=cookies,headers=headers)
            elif method=="post":
                self.res = requests.post(url=url, data=param, cookies=cookies, headers=headers)
            elif method=="delete":
                self.res = requests.delete(url=url, data=param, cookies=cookies, headers=headers)
        except Exception as e:
            raise e

    def get_status_code(self):
        return self.res.status_code

    def get_text(self):
        return self.res.text

    def get_json(self):
        json_dict=self.res.json()
        # # 通过json.dumps函数将字典转换成格式化后的字符串
        res_text=json.dumps(json_dict,ensure_ascii=False,indent=4)
        print("response:",res_text)
        return json_dict

    def get_cookies(self,key=None):
        # print(self.res.cookies)
        if key is not None:
            return self.res.cookies[key]
        else:
            return self.res.cookies











