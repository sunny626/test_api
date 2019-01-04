# _*_coding:utf-8 _*_
# @Time     :2019/1/1 0:30
# @Author   :sunny
# @Email    :602992114@qq.com

import unittest
import json
from api_test_sunny.common.request import Requests
from api_test_sunny.common.do_excel import DoExcel
from api_test_sunny.common import constant
from ddt import ddt,data
from api_test_sunny.common.mysql import MySqlUtil

do_excel = DoExcel(constant.test_data_dir)
cases = do_excel.get_cases("register")

@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取最大手机号码
        global mysql
        mysql=MySqlUtil()
        sql = "select MobilePhone from future.member where MobilePhone != '' ORDER BY MobilePhone DESC LIMIT 1"
        global max_phone
        max_phone=mysql.fetch_one(sql)["MobilePhone"]

    # def setUp(self):
    #     # 获取最大手机号码
    #     self.mysql=MySqlUtil()
    #     self.sql = "select MobilePhone from future.member where MobilePhone != '' ORDER BY MobilePhone DESC LIMIT 1"
    #     self.max_phone=self.mysql.fetch_one(self.sql)["MobilePhone"]

    @data(*cases)
    def test_register(self,case):
        data=json.loads(case.param)
        if data["mobilephone"]=="${register}":
            data["mobilephone"]=int(max_phone) + 1# 取到数据库里最大的手机号码进行加1来注册
        res = Requests(method=case.method, url=case.url, param=data)
        print("status_code:", res.get_status_code())
        res_dict=res.get_json() # 获取请求响应，字典
        print("response:",res_dict)
        self.assertEqual(case.expected,res.get_text())
        if res_dict["code"]==20010: # 注册成功的数据，判断数据库有这条数据
            sql='select MobilePhone from future.member where MobilePhone="{0}"'.format(self.max_phone)
            print(sql)
            expected=int(max_phone)+1
            member=mysql.fetch_one(sql)
            if member is not None:
                self.assertEqual(expected,member["mobilephone"])
            else:
                raise AssertionError
    #
    # def tearDown(self):
    #     self.mysql.close()

    @classmethod
    def tearDownClass(cls):
        mysql.close()






