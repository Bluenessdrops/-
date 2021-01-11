import random


def modify(loopNum, seq, lists):
    '''选号&修改列表&排序'''
    for _ in range(loopNum):
        num = random.choice(seq)
        seq.remove(num)
        lists.append(num)
    lists.sort()
    return lists


def daletou(extraFront, extraBehind, l_front  = [], l_behind = [], ll = []):
    ''' 大乐透模拟选号 '''
    seq1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    seq2 = [1,2,3,4,5,6,7,8,9,10,11,12]
    
    l_front  = modify(5, seq1,  l_front)
    l_behind = modify(2, seq2, l_behind)

    for i in l_front:
        i = '%02d' %int(i)
        ll.append(i)

    if extraFront == 3:
        extraFront = '%02d' %random.choice(seq1)
        ll.append(f'({extraFront})')    
    
    ll.append('+')

    for i in l_behind:
        i = '%02d' %int(i)
        ll.append(i)
        
    if extraBehind == 3:
        extraBehind = '%02d' %random.choice(seq2)
        ll.append(f'({extraBehind})') 

    return ll
