# coding:UTF-8

import os


class SplitText():  #.txt文件切分
    def __init__(self, file_name, file_num):
        """
        分割.txt文件
        :param file_name:
        :param file_num:
        """
        self.file_name = file_name
        part_line_num = self.get_file_line(file_name)
        self.file_num = int(part_line_num / file_num)

    def split_file(self):
        if self.file_name and os.path.exists(self.file_name):
            try:
                with open(self.file_name) as f:
                    temp_count = 0
                    temp_content = []
                    temp_num = 1
                    for line in f:
                        if temp_count < self.file_num:
                            temp_count += 1
                        else:
                            self.write_file(temp_num,temp_content)

                            temp_count = 1
                            temp_num += 1
                            temp_content = []

                        temp_content.append(line)
                    else:
                        self.write_file(temp_num,temp_content)
            except IOError as error:
                print (error)

    def get_part_file_name(self,part_num):
        temp_path = os.path.dirname(self.file_name)
        part_file_name = temp_path + "/temp_part_file"
        if not os.path.exists(part_file_name):
            os.makedirs(part_file_name)
        part_file_name = part_file_name + r"/" + str(part_num) + ".txt"
        print part_file_name
        return part_file_name

    def write_file(self,part_num,part_content):
        part_file_name = self.get_part_file_name(part_num)
        try:
            with open(part_file_name,"w") as part_file:
                for line in part_content:
                    part_file.write(line)

                print "Write successfully!"
        except IOError as error:
            print (error)

    def get_file_line(self,file_name):
        try:
            f = open(file_name)
            file = f.readlines()
            f.close()
            return len(file)
        except IOError as error:
            print (error)

# if __name__ == "__main__":
#     sf = SplitText(r"C:/Users/SunWeiWei/Desktop/1.txt",5)
#     sf.split_file()

