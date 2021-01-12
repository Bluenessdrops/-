import random


def modify(loopNum, seq, lists, ll, extraNum):
    '''选号&修改列表&排序'''
    lists = []
    #选择loopNum个不重复的号并排序
    for _ in range(loopNum):
        num = random.choice(seq)
        seq.remove(num)
        lists.append(num)
    lists.sort()

    #添加到下注列表
    for i in lists:
        ll.append('%02d' %int(i))

    #(可选)追加一位数
    if  extraNum == 3:
        extraNum = '%02d' %random.choice(seq)
        ll.append(f'({extraNum})') 


def splto(extraFront, extraBehind):
    ''' 模拟选号 '''
    ll    = []
    l_R_B = []
    seq1  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    seq2  = [1,2,3,4,5,6,7,8,9,10,11,12]

    #选出5个红球(可追加1位)和2个蓝球(可追加1位)
    modify(5, seq1, l_R_B, ll, extraFront)
    ll.append('+')
    modify(2, seq2, l_R_B, ll, extraBehind)

    return ll   

