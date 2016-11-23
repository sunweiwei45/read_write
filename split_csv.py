# coding:UTF-8

import os
import csv


class SplitCSV():  #.csv文件切分
    def __init__(self, file_name=None, file_num=None):
        """
        csv文件切分，如果无法均分，则多出一个文件存储均分后剩余的
        :param file_name: 需要切分的文件的具体位置
        :param file_num: 需要切分的数目
        """
        self.file_name = file_name
        part_line_num = self.get_file_line(file_name)
        self.file_num = int(part_line_num / int(file_num))

    def split_file(self):
        """
        CSV文件切分，结果到路径的/temp_part_file文件夹中
        :return:
        """
        if self.file_name and os.path.exists(self.file_name):
            #判断路径和文件存在
            try:
                with open(self.file_name, 'rb') as csvfile:
                    #将.csv文件分段
                    read = csv.reader(csvfile)
                    temp_count = 0
                    temp_content = []
                    temp_num = 1
                    for line in read:
                        if temp_count < self.file_num: #将该行数据加入列表直到列表行数满了
                            temp_count += 1
                        else:
                            self.write_file(temp_num, temp_content)  #将分好的文件存储
                            temp_count = 1
                            temp_num += 1
                            temp_content = []

                        temp_content.append(line)
                    else:
                        self.write_file(temp_num, temp_content)  #写入文件
            except IOError as error:
                print (error)

    def get_part_file_name(self, part_num):
        """
        设计分割后文件的存储路径
        :param part_num: (int) 第几份文件
        :return:(string) 文件具体路径
        """
        temp_path = os.path.dirname(self.file_name)
        part_file_name = temp_path + "/temp_part_file"
        if not os.path.exists(part_file_name):
            os.makedirs(part_file_name)
        part_file_name = part_file_name + r"/" + str(part_num) + ".csv"
        print part_file_name
        return part_file_name

    def write_file(self, part_num, part_content):
        """
        文件写入
        :param part_num:(int) 第几份文件
        :param part_content:(list<list>) 该份文件的内容
        :return:
        """

        part_file_name = self.get_part_file_name(part_num)
        try:
            with open(part_file_name, "wb") as csvfile:
                write = csv.writer(csvfile)
                write.writerows(part_content)
                print "Write successfully!"
        except IOError as error:
            print (error)

    def get_file_line(self, file_name):
        #获得文件行数
        try:
            f = open(file_name)
            file = f.readlines()
            f.close()
            return len(file)
        except IOError as error:
            print (error)

if __name__ == "__main__":
    sf = SplitCSV(file_name=r"E:/Sunweiwei/eHealth/yifan/statistics/question_doc/urls/page_urls_all.csv", file_num=5)
    sf.split_file()