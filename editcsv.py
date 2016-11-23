# coding:UTF-8

import csv

f = open("C:/Users/SunWeiWei/Desktop/goods.txt", "r")
s = f.readlines()    #按行读取文本中全部的数据
f.close()
data = []
for line in s:      #将数据存与列表中
    # print type(line)
    temp1 = line.decode("utf-8").strip("\n")  #解码并去除换行符
    temp2 = temp1.split(' ')              #建模每行数据用空格分块存与列表中
    # for s in temp2:
    #     print s.decode("utf8")
    data.append(temp2)
# print len(data)
csvfile = file('C:/Users/SunWeiWei/Desktop/good.csv', 'wb') #以二级制写的模式打开.csv文件
writer = csv.writer(csvfile)
#写表头
# writer.writerow(['XH','YC','YF','HZ','JB','JZDF','SJ','LX','TD','SFYCK','TJ','HY','PAGEURL','JZDFGXXS','JZDFLWZS','NR','ZQSJ','GRXXY'])
writer.writerow(['medicine_id','medicine_name','medicine_license_numbe'])
writer.writerows(data)
csvfile.close()

#
# f = open("C:/Users/SunWeiWei/Desktop/2.txt","w")
# u = s
# f.write(u)
# f.close()







