# time和datetime模块

"""
time:提供的功能是更加接近于操作系统层面的
datetime:比time高级了不少, 可以理解为datetime基于time进行了封装,提供了更多实用的函数
"""

from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()
print("now = ", now, ", 类型是",type(now))

# 获取指定时间
last = datetime(1994, 2, 2, 0, 0, 0)
print("last = ", last)

# 转换时间timestamp
last_timestamp = datetime.timestamp(last)
print("last_timestamp = ",last_timestamp, ", 类型是",type(last_timestamp))

# timestamp转换成datetime
print(datetime.fromtimestamp(last_timestamp))

# 时间加减
tomorrow = now + timedelta(hours=24)    # 加上24小时
print("tomorrow = ", tomorrow)

# 其他功能
print(now.isoweekday())     # 查看星期几
print(now.year)             # 查看年份