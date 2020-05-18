# raise和assert语句

num = input("请输入数字")

if not num.isdigit():
    raise Exception("你输入的不是数字")

assert int(num) > 100, "输入的数字太大"
