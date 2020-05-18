# 1.计算字符串最后一个单词的长度，单词以空格隔开。
def count_last_word():
    text = input("请输入文章")
    text_list = text.split(" ")
    count = 0
    if len(text_list):
        word = text_list[-1]
        count = len(word)

    print(count)


# 2.写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写
def count_char():
    text = input("请输入字符串").lower()
    char = input("请输入一个字符").lower()
    if len(text) < 1 or len(char) != 1:
        print("输入错误")
        return
    count = text.count(char)
    print(count)


# 3.明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），
# 对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好
# 的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。
def distinct_and_sort():
    n = int(input("请输入生成的个数"))
    res = set()
    for i in range(n):
        num = int(input("请输入第{}个数字".format(i + 1)))
        res.add(num)
    res = list(sorted(res))
    print(res)


# 4.• 连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
#   • 长度不是8整数倍的字符串请在后面补数字0，空字符串不处理
def cut_string(string):
    long = len(string)
    if long == 0:
        return
    elif long <= 8:
        print(string + "0" * (8 - long))
    else:
        print(string[:8])
        cut_string(string[8:])


# 5.写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入 ）
def sixteen_to_ten():
    num = True
    while num:
        num = input("请输入十六进制数字,按回车键退出")
        try:
            print(int(num, 16))
        except:
            pass


# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）,最后一个数后面也要有空格
def factorization(num):
    for i in range(2, num+1):
        if num % i == 0:
            print(i, end=" ")
            if num != i:
                factorization(int(num/i))
            break


if __name__ == '__main__':
    # count_last_word()
    # count_char()
    # distinct_and_sort()
    # cut_string("+646+441866+8354786fsfsf568+6834789387468wefriayiaggss")
    # sixteen_to_ten()
    factorization(72)
