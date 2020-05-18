def first():
    print("--------------------------")
    print("--------1.查看成绩--------")
    print("--------2.添加成绩--------")   
    print("--------3.退出系统--------")
    print("--------------------------")

def add():
    pass

def show():   
    with open("成绩.txt","r",encoding="utf8") as f:
        print("--------------------------")
        for line in f:
            lst = line.strip().split(",")
            print("| ",end="")
            print(lst[0],end="")
            print(" "*(8-len(lst[0])*2),end="")
            print(" | ",end="")
            print(lst[1],end="")
            print(" | ",end="")
            print(lst[2],end="")
            print(" "*(3-len(lst[2])),end="")
            print(" |")
        print("--------------------------")
            
