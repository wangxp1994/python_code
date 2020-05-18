
# 海象运算符
def one():
    a = [100,200,300]
    if (n := len(a)):
        print(n)

# f-string
def two():
    a = "你好"
    b = "世界"
    # 以前打印形式
    print(f"a={a},b={b}")
    # 新的打印形式
    print(f"{a=},{b=}")


# 传参"/"和"*"
def three(a,b,/,c,d,*,e):
    pass




if __name__ == '__main__':
    one()
    two()
    three(1,2,3,4,e=5)