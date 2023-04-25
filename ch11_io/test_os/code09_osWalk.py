# coding=utf-8
"""
测试os.walk()递归遍历所有的子目录和子文件
"""

import os


def test01():
    all_folder = []
    all_files = []
    path = os.getcwd()
    list_files = os.walk(path)
    for dirpath, dirnames, filenames in list_files:
        for dir in dirnames:
            all_folder.append(os.path.join(dirpath, dir))
            # print(os.path.join(dirpath,dir))
        # print("*****************")
        for file in filenames:
            all_files.append(os.path.join(dirpath, file))
            # print(os.path.join(dirpath,file))

    # 打印所有子目录
    for dir in all_folder:
        print(dir)

    print("***************")
    # 打印所有子文件
    for file in all_files:
        print(file)


if __name__ == '__main__':
    test01()
