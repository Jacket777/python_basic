#coding=utf-8
"""
测试os,path中关于目录，路径的操作
"""

import os
import os.path  #from os import path

# 判断：绝对路径，是否目录，是否文件，文件是否存在
def test01():
    print(os.path.isabs("d:/pythonworkspace/code01_flower.py"))  # True
    print(os.path.isdir("d:/pythonworkspace/code01_flower.py"))  # False
    print(os.path.isfile("d:/pythonworkspace/code01_flower.py"))  # False
    print(os.path.exists("d:/pythonworkspace/code01_flower.py"))


# 获取文件信息
def test02():
    print(os.path.getsize("b.txt"))
    print(os.path.abspath("b.txt"))
    print(os.path.dirname("d:/pythonworkspace/code01_flower.py"))

    print(os.path.getctime("b.txt"))  # 创建时间
    print(os.path.getatime("b.txt"))  # 访问时间
    print(os.path.getmtime("b.txt"))  # 修改时间




# 路径操作
def test03():
    path = os.path.abspath("b.txt")
    print(os.path.split(path))
    print(os.path.splitext(path))

    print(os.path.join("aa", "bb", "cc"))


# 列出工作目录下所有.py文件，并输出文件名
def test04():
    path = os.getcwd()
    file_list = os.listdir(path)  # 列出子目录，子文件
    for filename in file_list:
        if filename.endswith("py"):
            print(filename, end="\t")

# 列出工作目录下所有.py文件，并输出文件名
def test05():
    path = os.getcwd()
    file_list = os.listdir(path)  # 列出子目录，子文件
    for filename in file_list:
        if filename.endswith("py"):
            print(filename, end="\t")

    print("###################")
    file_list2 = [filename for filename in os.listdir(path) if filename.endswith("py")]
    for f in file_list2:
        print(f, end="\t")


if __name__ == '__main__':
    test01()





