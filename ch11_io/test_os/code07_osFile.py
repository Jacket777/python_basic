#coding=utf-8
"""
测试os模块中，关于文件和目录的操作
"""

import os

# 获取文件和文件的信息
def test01():
    print(os.name)  # 获得操作系统信息windos->nt linux unix->posix
    print(os.sep)  # 分割符windos->\  linux unix-->/
    print(repr(os.linesep))  # 换行符window->|r|n  linux-->|n
    print(os.stat("code07_osFile.py"))







# 关于工作目录的操作
def test02():
    print(os.getcwd())
    os.chdir("d:")  # 改变工作目录
    os.mkdir("book")  # 创建目录



# 创建目录，创建多级目录，删除####
def test03():
    os.mkdir("book")  # 创建目录
    os.rmdir("book")  # 删除目录 相对路径是对于当前工作目录
    os.makedirs("file/film/people")  # 创建多级目录
    os.removedirs("file/film/people")  # 删除多级目录，只能删除空目录
    os.makedirs("../music/Hongkong/hua")  # ..表示上级目录
    os.rename("book", "书")  # 修改文件名
    dirs = os.listdir("../music")
    print(dirs)









if __name__ == '__main__':
    test01()

