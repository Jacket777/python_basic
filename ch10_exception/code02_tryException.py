# coding=utf-8

# 实例：循环输入数字，如果不是数字，则处理异常，直到输入88，则结束循环
def test01():
    while True:
        try:
            x = int(input("请输入一个数字   "))
            print("输入的数字: ", x)
            if x == 88:
                print("退出程序")
                break
        except BaseException as e:
            print(e)
            print("异常，输入的不是一个数字")

    print("循环数字输入程序结束！")


# 测试try...多个except结构
def test02():
    try:
        a = input("请输入一个被除数： ")
        b = input("请输入一个除数： ")
        c = float(a) / float(b)
        print(c)

    except ZeroDivisionError:
        print("异常，不能除以0")
    except ValueError:
        print("异常，不能将字符串转为数字")
    except NameError:
        print("异常，变量不存在")
    except BaseException as e:
        print(e)


# 测试try..except..else结构
def test03():
    try:
        a = input("请输入一个被除数： ")
        b = input("请输入一个除数： ")
        c = float(a) / float(b)
    except BaseException as e:
        print(e)
    else:
        print("结果是 ", c)

if __name__ == '__main__':
    test01()
