
'''
已经完美搞定, 通过return_all参数来控制是否需要找全!

'''

def kmp(mom_string, son_string,return_all=False):
    # 传入一个母串和一个子串
    # 返回子串匹配上的第一个位置，若没有匹配上返回-1
    # 首先是合法性检验!!!!!!!!!!!!!!!!!!!!!!!
    test = []
    # if type(mom_string) != type(test) or type(son_string) != type(test):
    #     return -1
    if len(son_string) == 0:
        return 0
    if len(mom_string) == 0:
        return -1





    # 针对sonstring计算next数组.
    # 求next数组
    next = [-1] * len(son_string)
    if len(son_string) > 1:  # 这里加if是怕列表越界
        next[1] = 0
        i, j = 1, 0
        while i < len(son_string) - 1:  # 这里一定要-1，不然会像例子中出现next[8]会越界的
            if j == -1 or son_string[i] == son_string[j]: # 如果next数组匹配到了
                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
    if not return_all: # 下面这段是返回第一个符合的index的逻辑代码.
        # kmp框架
        m = s = 0  # 母指针和子指针初始化为0
        while (s < len(son_string) and m < len(mom_string)):
            # 匹配成功,或者遍历完母串匹配失败退出
            if s == -1 or mom_string[m] == son_string[s]: # 表示当前2个指针对应字符相通,匹配陈宫.所以都向后便宜一个.
                m += 1
                s += 1
            else:
                s = next[s]

        if s == len(son_string):  # 匹配成功
            return m - s
    else:
        # kmp框架
        save=[]
        m = s = 0  # 母指针和子指针初始化为0
        while m < len(mom_string):
            # 匹配成功,或者遍历完母串匹配失败退出
            if s == len(son_string):  # 匹配成功
                save.append(m - s)
                s=0
            if s == -1 or mom_string[m] == son_string[s]: # 表示当前2个指针对应字符相通,匹配陈宫.所以都向后便宜一个.
                m += 1
                s += 1

            else:
                s = next[s]
        if s == len(son_string):  # 用来匹配最末未的一个陪陪成功的时候.
            save.append(m - s)
        return save


    # 匹配失败
    return -1


# 测试
if 0:
    mom_string = 'fdsfasd'
    son_string = 'f'
    print(kmp(mom_string, son_string))
    print(kmp(mom_string, son_string,return_all=True))