
"""
上下文代码管理器
"""

import time

class count(object):
    def __init__(self,word):
        # 避免类初始化时大量重复的赋值语句
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
    def __enter__(self):
        self.t0 = time.time()
    def __exit__(self, *args):
        self.t1 = time.time()
        print(self.t1-self.t0)
        print(self.word)


if __name__ == '__main__':
    with count("周杰伦"):
        time.sleep(2)
