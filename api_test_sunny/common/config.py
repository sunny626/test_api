# _*_coding:utf-8 _*_
# @Time     :2018/12/31 14:17
# @Author   :sunny
# @Email    :602992114@qq.com
# function  :配置文件的读取

import configparser
import os
from api_test_sunny.common import constant

class ConfigLoader:

    def __init__(self):
        # 创建对象
        self.conf=configparser.ConfigParser()
        # 加载配置文件
        file_name=os.path.join(constant.configs_dir,"global.conf")
        self.conf.read(filenames=file_name)
        if self.conf.getboolean("switch","on"):
            online=os.path.join(constant.configs_dir,"online.conf")
            self.conf.read(filenames=online)
        else:
            test=os.path.join(constant.configs_dir,"test.conf")
            self.conf.read(filenames=test)

    def get(self,section,option):
#        通过section，option 来取到配置项的值
        return self.conf.get(section,option)

    def getboolean(self,section,option):
        return self.conf.getboolean(section,option)

    def getint(self,section,option):
        return self.conf.getint(section,option)

    def getfloat(self,section,option):
        return self.conf.getfloat(section,option)

if __name__ == '__main__':
    conf=ConfigLoader()
    url_pre=conf.get("api","url_pre")
    print(url_pre)
    print(type(url_pre))



