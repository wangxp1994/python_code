
import pandas as pd
from pandas import Series, DataFrame

filename = "demo.xls"

# 读取表格
def Excel():
    data = pd.read_excel(filename, sheet_name="sheet_name")

    # print (type(data))
    # print (data.values)
    # for i in data.values:
    #     print (i[1])

# Excel()

# Series
def Series_():

    s = Series(["wang", "cheng", 520])
    # print s

    # 自定义索引
    s = Series(["wangcheng", "man", 26], index=["name", "sex", "age"])
    s["name"] = "wangxiaopeng"
    print (s)

# Series_()

# DataFrame
def DataFrame_():
    # 也可以用字典套字典
    data = {"name":["Alibaba", "Baidu", "Tencent"],
            "marks":[100, 200, 300],
            "price":[1, 2, 3]}

    f1 = DataFrame(data)
    # print f1

    # 自定义索引
    f2 = DataFrame(data, columns=["name", "marks", "price", "sex"], index=["one", "two", "three"])

    # f2["sex"] = "male"
    # f2["sex"] = Series(["female", "male", "male"], index=["one", "two", "three"])
    # f2["price"]["two"] = 4

    print (f2)

DataFrame_()