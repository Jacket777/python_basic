#coding=utf-8
# 递归打印所有的目录和文件
import os

allfiles = []
def getAllFile(path,level):

    childFiles = os.listdir(path)
    for file in childFiles:
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            getAllFile(filepath,level+1)
        #print("\t"*level+filepath)
        allfiles.append("\t"*level+filepath)
        #print(file)

def test01():
    getAllFile("", 0)
    for f in reversed(allfiles):
        print(f)

if __name__ == '__main__':
    test01()


