from itertools import permutations, product

# 计算24点

# 主函数
def main():
    num_list = get_num()
    all_list = create_all_list(num_list)
    calculate_list = create_calculate_list()
    success_flag = False
    for i in all_list:
        for j in calculate_list:
            compute_str = "((a{}b){}c){}d".format(*j)
            sum = eval(compute_str,{"a":i[0],"b":i[1],"c":i[2],"d":i[3]})
            if sum == 24:
                compute_str = "(({}{}{}){}{}){}{}=24".format(i[0],j[0],i[1],j[1],i[2],j[2],i[3])
                print(compute_str)
                success_flag = True
                break
        if success_flag:
            break
    else:
        print("没有答案!")

# 获取四个数字
def get_num():
    num_list = []
    for i in range(4):
        num = input_num(i)
        num_list.append(num)
    return num_list

# 输入数字
def input_num(i):
    while True:
        try:
            num = int(input("请输入第{}个数字\t".format(i+1)))
            return num
        except:
            print("你输入的不是数字哦")

# 生成所有顺序
def create_all_list(num_list):
    all_list = list(permutations(num_list))
    return all_list

# 生成所有计算的顺序
def create_calculate_list():
    calculate_elements = "+-*/"
    calculate_list = list(product(calculate_elements, repeat=3))
    return calculate_list

if __name__ == '__main__':
    main()
