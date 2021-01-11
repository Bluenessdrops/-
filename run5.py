import rep
import datetime 
now_time = datetime.datetime.now().strftime('%F %T')
filePath = "E:/Kinlrmi.Clevorihno/Pictures/Onedrive/vscode/123.txt"
# sys.setrecursionlimit(3333) # 设置最大递归深度为3000

def headInfo(filePath, length):
    '''写入时间信息'''

    file = open(filePath,'a')
    file.write("\n")
    for _ in range(length):
        file.write('-')
    file.write('\n')
    file.write(f"- {now_time} ")
    for _ in range(length - 22):
        file.write('-')
    file.write('\n')
    for _ in range(length):
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
    
def getLength(data, length = 1):
    '''获取单条数据长度'''
    for ix in range(len(data)):
        s = str(data[ix]).replace('[','').replace(']','')
        s = s.replace("'",'').replace(',','') + ' '
        length += len(s)

    return length

def main (sym_list = []):

    for loopNum in range(3):
        if loopNum == 0:
            text = ' how many times?'
        elif loopNum == 1:
            text = ' extra frontNum? \n(Enter = yes)'
        elif loopNum == 2:
            text = ' extra behindNum? \n(Enter = yes)'
        symbol = input(f'{text} \n')
        if symbol == '':
            symbol = 3
        sym_list.append(symbol) 

    length = getLength(rep.daletou(sym_list[1], sym_list[2]))
    headInfo(filePath, length)

    for _ in range(int(sym_list[0])):
        bodyInfo(filePath, rep.daletou(sym_list[1], sym_list[2]))

    print('finished.')

main()
