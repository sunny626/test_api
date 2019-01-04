# _*_coding:utf-8 _*_
# @Time     :2018/12/31 16:37
# @Author   :sunny
# @Email    :602992114@qq.com

import unittest
import json
from api_test_sunny.common.request import Requests
from api_test_sunny.common.do_excel import DoExcel
from api_test_sunny.common import constant
from ddt import ddt,data
from api_test_sunny.common.basic_data import DoRegex
from api_test_sunny.common.basic_data import Context
from api_test_sunny.common.mysql import MySqlUtil

do_excel = DoExcel(constant.test_data_dir)
cases = do_excel.get_cases("recharge")

@ddt
class TestRecharge(unittest.TestCase):

    def setUp(self):
        # 充值前账户余额记录
        self.mysql=MySqlUtil()
        # 查询投资用户的账户信息
        self.sql="select * from future.member where mobilephone={0}".format(Context.normal_user)
        # 账户余额
        self.before_amount=self.mysql.fetch_one(self.sql)["LeaveAmount"]
        print("充值前的金额",self.before_amount)

    @data(*cases)
    def test_recharge(self,case):
        # 参数化处理
        data=DoRegex.replace(case.param)
        data=json.loads(data)
        if hasattr(Context,"cookies"):
            cookies=getattr(Context,"cookies")
        else:
            cookies=None
        res = Requests(method=case.method, url=case.url, param=data, cookies=cookies, headers=None)
        # 判断是否有cookie
        if res.get_cookies():
            setattr(Context,'cookies',res.get_cookies())
        print("status_code:", res.get_status_code())
        res_dict=res.get_json() # 获取请求响应，字典
        self.assertEqual(case.expected,int(res_dict["code"])) # 判断响应返回的code 是否与期望结果一致
        actual=self.mysql.fetch_one(self.sql)["LeaveAmount"] # 再次获取账户余额
        print("测试{}后的余额".format(case.case_description),actual)
        # 充值成功，判断余额增加
        if res_dict["code"]=="10001" and res_dict["msg"]=="充值成功":
            amount=float(data["amount"]) # 从参数data中取到充值金额
            print("充值金额{0}元".format(amount))
            expected=float(self.before_amount) + amount # 充值成功，期望余额=原来余额+充值金额
            self.assertEqual(expected,actual)
        elif res_dict["code"]!="10001":
            expected=self.before_amount  # 充值失败后，余额为增加
            self.assertEqual(expected,actual)
        if case.expected == int(res_dict["code"]):#写入actual和result的值
            print("pass")
            do_excel.write_text_by_case_id(sheet_name="recharge", case_id=case.case_id, actual=int(res_dict["code"]),
                                           result="pass")
        else:
            print("fail")
            do_excel.write_text_by_case_id(sheet_name="recharge", case_id=case.case_id, actual=int(res_dict["code"]),
                                           result="fail")

    def tearDown(self):
        self.mysql.close()
