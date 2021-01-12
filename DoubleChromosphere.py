import random


def dblCrmsphe(extraRed, extraBlue):
    ''' 模拟选号 '''
    listR_B  = []
    seq_Red  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
    seq_Blue = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    #选出6个不重复的红球添加到下注列表
    for _ in range(6):
        redNum = random.choice(seq_Red)
        seq_Red.remove(redNum)
        listR_B.append('%02d' %redNum)
    listR_B.sort()

    #(可选)追加1个红球
    if extraRed == 3:
        extraNum = '%02d' %random.choice(seq_Red)
        listR_B.append(f'({extraNum})') 

    #选出1个蓝球并添加到下注列表
    blueNum = random.choice(seq_Blue)
    listR_B.append('+')
    listR_B.append('%02d' %blueNum)

    #(可选)追加1个蓝球
    if extraBlue == 3:
        seq_Blue.remove(blueNum)
        extraNum = '%02d' %random.choice(seq_Blue)
        listR_B.append(f'({extraNum})') 

    return listR_B

