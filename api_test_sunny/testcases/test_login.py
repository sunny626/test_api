# _*_coding:utf-8 _*_
# @Time     :2018/12/31 15:51
# @Author   :sunny
# @Email    :602992114@qq.com

import unittest
import json
from api_test_sunny.common.request import Requests
from api_test_sunny.common.do_excel import DoExcel
from api_test_sunny.common import constant
from ddt import ddt,data
from api_test_sunny.common import logger

do_excel = DoExcel(constant.test_data_dir)
cases = do_excel.get_cases("login")

@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        print("登录开始")

    @data(*cases)
    def test_login(self,case):
        data=json.loads(case.param)
        res = Requests(method=case.method, url=case.url, param=data, cookies=None, headers=None)
        print("status_code:", res.get_status_code())
        res_dict=res.get_json() # 获取请求响应，字典
        print("response:",res_dict)
        self.assertEqual(case.expected,res.get_text())
        if case.expected == res.get_text():#写入actual和result的值
            print("pass")
            do_excel.write_text_by_case_id(sheet_name="login", case_id=case.case_id, actual=res.get_text(),
                                           result="pass")
        else:
            print("fail")
            do_excel.write_text_by_case_id(sheet_name="login", case_id=case.case_id, actual=res.get_text(),
                                           result="fail")

    def tearDown(self):
        print("测试清除")











