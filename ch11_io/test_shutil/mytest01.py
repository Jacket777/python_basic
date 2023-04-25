#coding=utf-8
#测试shutil模块的用法:拷贝，压缩
import shutil
import zipfile

#shutil.copyfile("test01.txt","test01_copy.txt") #拷贝文件
#shutil.copytree("movie/CHN","电影")  #拷贝目录
#shutil.copytree("movie/CHN","电影",ignore=shutil.ignore_patterns("*.txt","*.html"))

#压缩与解压缩
#shutil.make_archive("电影/gg","zip","movie/CHN/HK")

#压缩
#z1 = zipfile.ZipFile("a.zip","w")
#z1.write("test01.txt")
#z1.write("test01_copy.txt")
#z1.close()

#解压缩
z2 = zipfile.ZipFile("a.zip","r")
z2.extractall("电影")
z2.close()
