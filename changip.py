# coding:UTF-8

import json
import os
import time
import random

class ChangeJson():
    """
    使用shadowsocks自动修改ip
    """
    def __init__(self, json_in, json_out):
        self.json_in = json_in
        self.json_out = json_out

    def change_json(self, key, value):
        if os.path.exists(self.json_in) and self.json_in:
            #验证路径和问价是否存在
            try:
                with open(self.json_in, 'r') as json_file:
                    #读取json的文件
                    data = json.load(json_file)
                data[key] = value
                with open(self.json_out, 'w') as json_file:
                    #写入json
                    newjson = json.dumps(data, sort_keys=True, indent=4)
                    json_file.write(newjson)
            except Exception as e:
                #异常处理
                print e
        else:
            print "The path is not exit"

if __name__ == "__main__":
    while True:
        os.startfile("F:\ss\Shadowsocks.exe")  #Shadowsocks 的位置
        time.sleep(7200)  #设置切换ip的时间间隔
        os.system('taskkill /f /im Shadowsocks.exe')  #启动Shadowsock
        index = random.randint(0, 6)
        cj = ChangeJson(r"F:/ss/gui-config.json", r"F:/ss/gui-config.json")
        cj.change_json('index', index)












