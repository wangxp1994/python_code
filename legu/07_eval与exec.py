
# eval(expression,[,globals[,locals]])
# 计算指定表达式
x = 10 
def fx1():
    y = 20
    a = eval("x+y")
    print("a:", a)
    b = eval("x+y", {"x":1, "y":2})
    print("b:", b)
    c = eval("x+y", {"x":1, "y":2}, {"y":3, "z":4})
    print("c:", c)
    
fx1()

# exec(object,[,globals[,locals]])
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def fx2():
    y = 20
    exec(expr)
    exec(expr,{"x":1,"y":2})
    exec(expr,{"x":1,"y":2},{"y":3,"z":4})

fx2()