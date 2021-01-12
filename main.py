import datetime 


#写入log的完整路径
#请自行补全
filePath = "E:/xxx/vscode/play&log.txt"


def headInfo(filePath, length, gamble_kind):
    '''写入时间和玩法信息'''
    now_time = datetime.datetime.now().strftime('%F %T')
    file = open(filePath,'a')
    file.write("\n")

    for _ in range(length):
        file.write('-')
    file.write('\n')
    
    file.write(f"- {now_time} ")
    for _ in range(length - 22):
        file.write('-')
    file.write('\n')

    file.write(f"- {gamble_kind} ")
    for _ in range(length - 13):
        file.write('-')
    file.write('\n')
    file.close()


def bodyInfo(filePath, data):
    '''写入数据信息'''
    file = open(filePath,'a')
    file.write("- ")
    for ix in range(len(data)):
        s = str(data[ix]).replace('[','').replace(']','')
        s = s.replace("'",'').replace(',','') + ' '
        file.write(s)
    file.write("\n")
    file.close()
    

def main (sym_list = []):
    '''主程序'''

    for loopNum in range(4):
        if   loopNum == 0:
            text = ' 兄弟玩啥? \n(1.大乐透  2.双色球) \n(默认回车是大乐透) '
        elif loopNum == 1:
            text = ' 兄弟来几注? \n(默认回车是3注) '
        elif loopNum == 2:
            text = ' 追加红球不? \n(加一位摁回车) '
        elif loopNum == 3:
            text = ' 追加篮球不? \n(加一位摁回车) '

        symbol = input(f'{text} \n')
        if symbol == '':
            symbol = 3
        sym_list.append(symbol) 

    #根据输入选择选号程序
    if  sym_list[0] ==  '2':
        gamble_kind = 'DblChromos' 
        from DoubleChromosphere import dblCrmsphe as gamble
    else:
        gamble_kind = 'SuperLotto'
        from SuperLotto         import splto      as gamble

    #头部的虚线长度
    if   sym_list[2] == 3 and sym_list[3] == 3:
        length = 34
    elif sym_list[2] != 3 and sym_list[3] != 3:
        length = 24
    elif sym_list[2] != 3 or  sym_list[3] != 3:
        length = 29

    #写入头部
    headInfo(filePath, length, gamble_kind)

    #写入号码
    for _ in range(int(sym_list[1])):
        millionNum = gamble(sym_list[2], sym_list[3])
        bodyInfo(filePath, millionNum)

    print('号码已保存到LOG中')


main()
