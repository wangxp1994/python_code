from other import *

while True:
    first()
    try:
        sel = int(input("请选择?  "))
        if sel == 1:            
            show()
        elif sel == 2:
            add()        
        elif sel == 3:
            print("正在退出系统")
            break
    except Exception as e:
        pass