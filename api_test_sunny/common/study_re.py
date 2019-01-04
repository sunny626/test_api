# _*_coding:utf-8 _*_
# @Time     :2018/12/31 17:10
# @Author   :sunny
# @Email    :602992114@qq.com

import re
from api_test_sunny.common.config import ConfigLoader

# s='{"mobilephone":"${register}","pwd":"123456"}'
# pattern="13800000000" # 正则表达式
# res3=re.findall(pattern='(\d{11})',string=s)
# print(res3)
# mobilephone=res3[0]
# print(mobilephone)
# s=s.replace(mobilephone,"13800000001")
# print(s)
# res4=re.findall(pattern='\$\{(.*?)\}',string=s)
# print(res4)
# res5=re.sub(pattern='\$\{(.*?)\}',repl="123456",string=s)
# print(res5)

# s1="www.lemonban.com"
# p="(w)(ww)"# () 进行分组
# m=re.search(p,s1)
# print(m)
# print(m.group(0)) # 全匹配
# print(m.group(1)) # 取到第一个分组里面的字符
# print(m.group(2)) # 取到第二个分组里面的字符

from api_test_sunny.common.basic_data import Context
s='{"mobilephone":"${normal_user}","pwd":"${pwd}"}'
pattern = '\$\{(.*?)\}'
while re.search(pattern,s):
    m=re.search(pattern,s)
    print(m.group(1))
    key=m.group(1)
    user=getattr(Context,key)
    print(user)
    s=re.sub(pattern,user,s,count=1)
    print(s)







