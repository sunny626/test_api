# _*_coding:utf-8 _*_
# @Time     :2018/12/31 21:40
# @Author   :sunny
# @Email    :602992114@qq.com

import re

class DoRegex:

    @staticmethod
    def replace(target):
        pattern='\$\{(.*?)\}'
        while re.search(pattern, target):
            m = re.search(pattern, target)
            key = m.group(1)
            user = getattr(Context, key)
            target = re.sub(pattern, user, target, count=1)
        return target


from api_test_sunny.common.config import ConfigLoader

class Context:

    config=ConfigLoader()
    normal_user=config.get("basic","normal_user")
    pwd=config.get("basic","pwd")

    # def __init__(self,a,b):
    #     self.a=a
    #     self.b=b

if __name__ == '__main__':
    normal_user=getattr(Context,"normal_user") # 获取变量
    print(normal_user)
    setattr(Context,"admin","123456")
    admin=getattr(Context,"admin")
    print(admin)
    if hasattr(Context,"admin"):
        delattr(Context,"admin")
    else:
        print("没有这个属性，不执行删除")

    # context=Context(1,2)
    # print(getattr(context,"a"))
