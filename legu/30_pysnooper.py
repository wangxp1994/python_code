
import pysnooper
import random
from threading import Thread

a = 3
class B:
    pass

@pysnooper.snoop(prefix="")
# @pysnooper.snoop("debug.log")
# @pysnooper.snoop(prefix="funOne")
# @pysnooper.snoop(max_variable_length=None)

def one(n):
    sum_ = []
    b = B()
    for i in range(n):
        num = random.randint(1,100)
        sum_.append(num)
        b.name = i

    return sum_

# @pysnooper.snoop(prefix="funTwo")
def two(n):
    sum_ = 0
    for i in range(n):
        num = random.randint(1,100)
        sum_ += num

    return sum_



if __name__ == '__main__':

    # t = Thread(target=two, args=(6,))
    # t.start()
    one(5)
    # t.join()







