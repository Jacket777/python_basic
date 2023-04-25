#测试操作csv文件的读取和写入
import csv

def test01():
    with open("dd.csv", "r") as f:
        a_csv = csv.reader(f)
        # print(list(a_csv))
        for row in a_csv:
            print(row)



def test02():
    with open("ee.csv", "w") as f:
        b_csv = csv.writer(f)
        b_csv.writerow(["ID", "姓名", "年龄"])
        b_csv.writerow(["1001", "高一", 18])
        c = [["1002", "高二", 18], ["1003", "高三", 19]]
        b_csv.writerows(c)






