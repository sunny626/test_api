#-*- coding:utf-8 -*-
# author:sunny
# datetime:2019/1/2 0002 下午 3:25

import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from api_test_sunny.common import constant

discover=unittest.defaultTestLoader.discover(constant.testcases_dir, pattern='test*.py',top_level_dir=None)
with open(constant.report_html,mode='wb+') as file:
    sunny=HTMLTestRunner(stream=file,
                         verbosity=2,
                         title="API",
                         description="API测试报告",
                         tester="sunny")
    sunny.run(discover)

