# -*- coding:UTF-8 -*-
import json
import os
import time
import random


class ChangeJson():
    def __init__(self,json_in,json_out):
        """
        初始化
        :param json_in:(string),读入JSON文件的路径
        :param json_out:(string),写出JSON文件的路径
        """
        self.json_in = json_in
        self.json_out = json_out

    def change_json(self, key, value):
        if os.path.exists(self.json_in) and self.json_in:
            try:
                with open(self.json_in, 'r') as json_file:
                    data = json.load(json_file) #读JSON文件并解码到data
                    ##以下是改进的初步想法：将想要修改的JAON的具体位置用/表示，可以修改深层的JSON
                    # key = key.split('/')
                    # print key
                    # num = len(key)
                    # if num == 0:
                    #     print "key is wrong"
                    # elif num == 1:
                    #     data[key[0]] = value
                    # elif num == 2:
                    #     data[key[0]][key[1]] = value
                    # elif num == 3:
                    #     data[key[0]][key[1]][key[2]] = value
                    # elif num == 4:
                    #     data[key[0]][key[1]][key[2]][key[3]] = value
                    # elif num == 5:
                    #     data[key[0]][key[1]][key[2]][key[3]][key[4]] = value
                    # else:
                    #     print "your key is too long!!"
                data[key] = value
                with open(self.json_out, 'w') as json_file:
                    newjson = json.dumps(data, sort_keys=True, indent=4)  #将字符串编码成JSON格式
                    json_file.write(newjson)  #写入JSON
            except Exception as e:
                print e
        else:
            print "The path is not exit"

##使用该类修改JSON的例子——Shadowsocks
# if __name__ == "__main__":
#     for i in range(10):
#         os.startfile("D:\Shadowsocks-win-2.3\Shadowsocks.exe")
#         time.sleep(60)
#         os.system('taskkill /f /im Shadowsocks.exe')
#         index = random.randint(0,7)
#         # print index
#         cj = ChangeJson(r"D:/Shadowsocks-win-2.3/gui-config.json",r"D:/Shadowsocks-win-2.3/gui-config.json")
#         cj.change_json('index',index)



