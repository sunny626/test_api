# _*_coding:utf-8 _*_
# @Time     :2018/12/31 14:29
# @Author   :sunny
# @Email    :602992114@qq.com
# function  :常量管理 不会改变的变量

import  os

# os.path.abspath(__file__)获取到该模块的路径，
# os.path.dirname(os.path.dirname(os.path.abspath(__file__)))获取到项目的根路径
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

configs_dir=os.path.join(base_dir,"configs")
# print(configs_dir)

datas_dir=os.path.join(base_dir,"datas")
test_data_dir=os.path.join(datas_dir,"test_data.xlsx")
# print(datas_dir)

assertions_dir=os.path.join(base_dir,"assertions")
# print(assertions_dir)

logs_dir=os.path.join(base_dir,"logs")
log_file=os.path.join(logs_dir,"log.log")
# print(logs_dir)

reports_dir=os.path.join(base_dir,"reports")
report_html=os.path.join(reports_dir,"report.html")
# print(reports_dir)

testcases_dir=os.path.join(base_dir,"testcases")
# print(testcases_dir)




