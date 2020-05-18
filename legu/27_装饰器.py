
def libai(fun):
    def libai_song():
        fun()
        print('李白 - 朝辞白帝彩云间')
    return libai_song


def dufu(fun):
    def dufu_song():
        print('杜甫 - 岱宗夫如何?齐鲁青未了')
        fun()
    return dufu_song


@libai
@dufu
def old_fun():
    print('-------分界线-------')



if __name__ == '__main__':
    old_fun()