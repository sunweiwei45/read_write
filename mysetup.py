# coding:UTF-8

# mysetup.py
from distutils.core import setup
import py2exe

setup(console=["changip.py"])  #将非图形界面的的python(changip.py)文件打包成.exe格式的文件  在dist文件夹中
