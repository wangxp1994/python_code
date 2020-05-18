# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/05/18 9:46

import pymysql
import threading

# 连接本地数据库
class DB(object):
    _instance_lock = threading.Lock()
    def __init__(self, host=None, part=None, user=None, password=None, database=None, charset=None, place=None):
        if place:
            self.defaultConfig(place, database)
        else:
            self.setConfig(host, port, user, password, database, charset)

        self.connectDB()

    # 默认配置
    def defaultConfig(self, place, database=None):
        if place == "hanyue":
            config = {
                "host" : "localhost",
                "port": 3306,
                "user": "wxp",
                "password": "123456",
                "database": "test",
                "charset": "utf8"
            }
        elif place == "daily_cpde":
            config = {
                "host": "localhost",
                "port": 3306,
                "user": "wang",
                "password": "wxp520++",
                "database": "test",
                "charset": "utf8"
            }
        if database:
            config["database"] = database

        self.setConfig(**config)

     # 设置参数
    def setConfig(self, host, port, user, password, database, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    # 连接数据库, 创建光标
    def connectDB(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()
        print("--> 数据库{}已连接成功".format(self.database))

    # 执行sql语句,返回结果
    def execute(self, sql, isReturn=False):
        self.cursor.execute(sql)
        if isReturn:
            return self.cursor.fetchall()

    # 对象销毁时关闭数据库
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("--> 数据库已关闭")

    # 实现单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with DB._instance_lock:
                if not hasattr(cls, "_instance"):
                    DB._instance = object.__new__(cls)

        return DB._instance


if __name__ == '__main__':
    db = DB(place="hanyue")
    sql = "select * from student"

    result = db.execute(sql, 1)
    print(result)