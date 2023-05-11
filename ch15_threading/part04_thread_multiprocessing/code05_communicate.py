# -*-coding:utf-8 -*-
import os;
import sys;

# sys.getdefaultencoding()
# reload(sys)
# sys.setdefaultencoding('UTF-8');
#
# result = os.system("java")
# #print result.encode('gb2312')
#
# # status, output = commands.getstatusoutput('date')
# # print status    # 0
# # print output    # 2016年 06月 30日 星期四 19:26:21 CST

# value = '你好'
# print value.decode('UTF-8').encode('GBK')
command = 'java -jar F:\\HDFS-API-TEST-2.0-jar-with-dependencies.jar'

# r = os.popen(command)
#
# info = r.read()
# print '======================'
# for line in info:
#     line = line.strip('\r\n')
#     print line


# r = os.system(command)
# text = r.read()
# r.close()
# print text


import subprocess
import time

res = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# mi = res.stdout.readlines()
# for line in mi:
#     print line

# mi = float((mi[0].strip()))

# while True:
#     mi = res.stdout.readlines()
#     for line in mi:
#         print line
#     print "AAAAAAAAAAAAAAAAA"
#     res.stdout.flush()
#     time.sleep(4)
#     print "======================"

oc = res.communicate()
for line in oc:
    print
    line










