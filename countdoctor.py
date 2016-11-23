# coding:UTF-8

import csv
from use_mysql import UseMySQL#引入自己编写的处理mysql的类
from collections import Counter#引入Python自带处理统计次数的类

"""
功能：从数据库里读取数据，统计每个医生历年每个月的电话就诊数
时间：2016年10月28日18:53:07
后续：可以编写处理CSV文件的类
"""
with open(r"E:/Sunweiwei/eHealth/yuanyuan/doc_url.csv", "rb") as csvfile:
    #安全地打开文件
    read = csv.reader(csvfile)
    my_sql = UseMySQL()#实例化处理mysql数据库的类并建立连接，数据库设置等在配置文件mysql_setting中写好
    temp_coun = []
    for row in read:
        #依次处理每一个医生的url
        record = {
            'doctor_url': str(row[0])
        }
        select_result = my_sql.select_mysql(record)#查询返回一个医生所有的电话咨询记录，以字典列表的形式
        temp_list = []
        for dict in select_result:
            # 提取每一个医生电话问诊的年份和月份并放进一个列表
            time = str(dict['order_time']).split("-")
            ym = time[0]+time[1]
            temp_list.append(ym)
        count = Counter(temp_list)#使用python自带的counter函数来统计ym，返回字典
        result = []#最终的结果是一个列表，每一列是：医生url+ym+次数
        for key in count:
            #将一个医生的所有结果添加进列表
            temp = []
            temp.append(select_result[0]['doctor_url'])
            temp.append(str(key))
            temp.append(str(count[key]))
            result.append(temp)
        with open(r"E:/Sunweiwei/eHealth/yuanyuan/result_2.csv","ab+") as csvfile:
            #将结果写入result.csv中
            write = csv.writer(csvfile)
            write.writerows(result)


        with open(r"E:/Sunweiwei/eHealth/yuanyuan/dealed_2.csv", "ab+") as csvfile:
            #将处理过的doctor_url存储在dealed.csv中，以防意外
            write = csv.writer(csvfile)
            write.writerow(row)

        temp_coun.append(row[0])#将已经处理过的医生的url放入另一个暂时的表
        print "The " + result[0][0] + " is " + str(len(temp_coun))#输出处理进度
    my_sql.close_mysql()#关闭数据库连接

