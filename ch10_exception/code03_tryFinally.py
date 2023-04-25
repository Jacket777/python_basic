# 测试try...except...eles...finally结构
def test01():
    try:
        a = input("请输入一个被除数： ")
        b = input("请输入一个除数： ")
        c = float(a) / float(b)
    except BaseException as e:
        print(e)
    else:
        print("结果是 ", c)
    finally:
        print("我是finally中的语句，无论是否发生异常，都会执行")

    print("程序结束")


# 测试finally
def test02():
    try:
        f = open("d:/a.txt", "r")
        content = f.readline()
        print(content)
    except:
        print("文件未找到")
    finally:
        print("run in finally,关闭资源")
        try:
            f.close()
        except BaseException as e:
            print(e)

    print("程序执行结束")


if __name__ == '__main__':
    test01()

