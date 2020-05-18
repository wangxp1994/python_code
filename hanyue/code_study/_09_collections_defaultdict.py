
"""
default为字典查询提供了默认值
"""

from collections import defaultdict
from datetime import datetime

dic = defaultdict(lambda : datetime.now())
print(dic[1])
