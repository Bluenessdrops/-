import rep
import datetime 
now_time = datetime.datetime.now().strftime('%F %T')
filename = "E:/Kinlrmi.Clevorihno/Pictures/Onedrive/vscode/123.txt"
# sys.setrecursionlimit(3333) # 设置最大递归深度为3000

def overw(filename):

    file = open(filename,'a')
    file.write("\n")
    file.write("------------------------\n")
    file.write(f"- {now_time} --\n")
    file.write("------------------------\n")
    file.close()

def text_save(filename, data):
    
    file = open(filename,'a')
    file.write("- ")
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')
        s = s.replace("'",'').replace(',','') + ' '
        file.write(s)
    file.write("\n")
    file.close()

def main ():
    overw(filename)
    x = input('how many times? \n')
    if x == '':
        x = 3
    for _ in range(int(x)):
        milionNum = rep.daletou()
        # milionNum = rep.this()
        text_save(filename, milionNum)
    print('finished.')

main()
