# _*_coding:utf-8 _*_
# @Time     :2018/12/31 16:39
# @Author   :sunny
# @Email    :602992114@qq.com
# function  ：数据库操作封装类

"""
1:连接数据库
2：辨析额一个SQL
3：建立游标
4：执行
"""

import pymysql
from api_test_sunny.common.config import ConfigLoader

class MySqlUtil:

    def __init__(self):
        config=ConfigLoader()
        host=config.get("mysql","host")
        port = config.getint("mysql", "port")
        user = config.get("mysql", "usr")
        password = config.get("mysql", "pwd")
        self.mysql=pymysql.connect(host=host, user=user, password=password,
                        port=port,cursorclass=pymysql.cursors.DictCursor)

    def fetch_one(self,sql): # 查询一条数据并返回
        cursor=self.mysql.cursor()
        cursor.execute(sql) # 根据sql进行查询
        return cursor.fetchone() # 返回元组()

    def fetch_all(self,sql): # 查询一条数据并返回
        cursor=self.mysql.cursor()
        cursor.execute(sql)
        return cursor.fetchall() # 返回元组嵌套元组，((),())

    def close(self): # 关闭数据库
        self.mysql.close()

if __name__ == '__main__':
    sql = "select MobilePhone from future.member where MobilePhone != '' ORDER BY MobilePhone DESC LIMIT 1"
    print(sql)

    mysql=MySqlUtil()
    data=mysql.fetch_one(sql)
    print(type(data),data)
    # max_mobilephone=int(data[0])+1
    # print(max_mobilephone)
    print(data["MobilePhone"])





