#-*- coding:utf-8 -*-
# author:sunny
# datetime:2019/1/2 0002 上午 10:27

import logging
from api_test_sunny.common import constant

# 创建日志收集器
my_logger=logging.getLogger("sunny")
my_logger.setLevel("DEBUG")

# 指定日志输出格式
formtter=logging.Formatter("%(asctime)s-%(filename)s-%(lineno)s-%(levelname)s-日志信息：%(message)s")

# 指定输入渠道
# 控制台输出
console=logging.StreamHandler()
console.setLevel("DEBUG")
console.setFormatter(formtter)

# 文件输出
file=logging.FileHandler(filename=constant.log_file,encoding="utf-8")
file.setLevel("DEBUG")
file.setFormatter(formtter)
# 对接
my_logger.addHandler(console)
my_logger.addHandler(file)

if __name__ == '__main__':
    my_logger.debug("这是一个debug信息")
    my_logger.info("这是一个info信息")
