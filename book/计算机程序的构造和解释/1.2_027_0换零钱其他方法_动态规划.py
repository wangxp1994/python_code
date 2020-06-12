# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/10 14:29

def cc(amount, kinds_of_coins):
    kand_list = getKindList(kinds_of_coins)
    L = [i==0 for i in range(amount+1)]

    for i in range(kinds_of_coins):
        for j in range(kand_list[i], amount+1):
            L[j] += L[j - kand_list[i]]

    return L[amount]

def getKindList(kinds_of_coins):
    return [1,  5, 10, 25, 50][:kinds_of_coins]


if __name__ == '__main__':
    print(cc(100, 5))





