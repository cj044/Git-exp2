#打開文件


#請輸入數字
num=int(input('請輸入數字:'))
#新的文件內容
newcontent = ' '

with open ('filerw.txt',encoding='utf8')as f :
    infoList = f.readlines()

#循環讀取每一行，然後存到新的文件內容中
    for line in infoList:
        # 判斷Line 是否含有關鍵字串 av74(目標物)
        #print(line)
        if not 'tv74706411/?p ='in line:#如果沒有，就skip寫回去
            newcontent += line
            continue #繼續讀下一行
        else: #否則(如果有)將拆成三部分，以便擷取三段
            pos1 = line.find('tv74706411/?p=')#1.數字前面部分
            pos2 = pos1 + len('tv74706411/?p=')#2.數字部分(主要相加部分)
            part1 = line[:pos2]   #3.數字前面部分
            part2 = line[pos2:] #以pos2當作基準
            newnumber= ' ' #保存數字部分

            for ch in part2:
                if ch.isdigit():
                    newnumber += ch
                else:
                    break
            part3 = part2[len(newnumber):]#數字後
        #newline = 數字前+(數字+num)+數字後
            newline=part1 + str(int(newnumber)+num)+ part3
            newcontent += newline
#最後關檔案
with open ('a.txt','w',encoding='utf8')as f :
    f.write(newcontent)