import random

def daletou(extraFront, extraBehind, l_front  = [], l_behind = [], ll = []):
    ''' 大乐透模拟选号 '''

    seq1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    seq2 = [1,2,3,4,5,6,7,8,9,10,11,12]
        
    for i in range(5):
        front = random.choice(seq1)
        seq1.remove(front)
        l_front.append(front)

    for i in range(2):
        behind = random.choice(seq2)
        seq2.remove(behind)
        l_behind.append(behind)

    l_front.sort()
    l_behind.sort()

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
