
# format传参
def fx1():
    user = 'wang'
    action = 'buy'
    
    # log = 'User {} has logged in and did an action {}'.format(user, action)

    # log = f'User {user} has logged in and did an action {action}'

    # log = 'User {1} has logged in and did an action {0}'.format(action, user)

    # log = 'User {u} has logged in and did an action {a}'.format(a=action, u=user)

    # dic = {'user':user, 'action':action}
    # log = 'User {user} has logged in and did an action {action}'.format(**dic)
    # log = 'User {0[user]} has logged in and did an action {0[action]}'.format(dic)

    tup = (user,action)
    # log = 'User {} has logged in and did an action {}'.format(*tup)
    log = 'User {0[0]} has logged in and did an action {0[1]}'.format(tup)

    # print(log)

# 转换字段
def fx2():
    name = 'Bruce Lee 李小龙'

    # msg = 'I am {!s}!'.format(name)
    # msg = 'I am {!r}!'.format(name)
    msg = 'I am {!a}!'.format(name)

    print(msg)

# 格式说明符
def fx3():
    # {字段名!转换字段:格式说明符}
    # [[填充]对齐方式][正负号][#][0][宽度][分组选项][.精度][类型码]
    
    # msg = '{0:{1}}'.format(3.14159, '.4f')

    # [[填充]对齐方式][正负号][宽度][.精度]
    msg = '{:哇=+9.2f}'.format(3.14159)
    msg = '{:哇=-9.2f}'.format(-3.14159)

    print(msg)

# 时间
def fx4():
    from datetime import datetime

    msg = 'Today is : {:%a %b %d %H:%M:%S %Y}'.format(datetime.now())

    print(msg)

def fx5():
    a = [1,2,3,4]
    if len(a) > 2:
        print(f"a列表的长度大于2,长度为{len(a)}")


if __name__ == '__main__':
    # fx1()
    # fx2()
    # fx3()
    # fx4()
    fx5()

