
from pprint import pprint
from pathlib import Path

def fx1():
    p = Path(r'D:\pythonOther\python_2\o\t\1.app.txt')
    # 文件名
    name = p.name
    # 文件名无后缀
    stem = p.stem
    # 文件名后缀
    suffix = p.suffix
    # 文件名后缀们
    suffixs = p.suffixes
    # 相当于dirnanme
    parent = p.parent
    # 返回一个iterable, 包含所有父目录
    parents = list(p.parents) 
    # 将路径通过分隔符分割成一个元祖
    parts = p.parts
    # 文件详细信息
    stat = p.stat()
    # 文件大小
    size = stat.st_size
    # 创建时间
    ctime = stat.st_ctime
    # 修改时间
    mtime = stat.st_mtime

    pprint(locals())


def fx2():
    p1 = Path(r'D:\pythonOther\python_2\o')

    # 字符串拼接
    p2 = Path(p1, r't\1.app.txt')
    # 文件是否存在
    exists = p1.exists()
    # 判断是否是文件
    is_file = p2.is_file()
    # 判断是否是目录
    is_dir = p1.is_dir()
    # 遍历文件夹,迭代器
    iterdir = list(p1.iterdir())

    pprint(locals())

def fx3():
    p = Path(r'D:\pythonOther\python_2\o\t\h\er')
    # 创建文件目录(前提是tt目录存在, 否则会报错)
    # p.mkdir(exist_ok=True)  
    # 递归创建文件目录    
    p.mkdir(exist_ok=True, parents=True)    

if __name__ == '__main__':
    # fx1()
    # fx2()
    fx3()


