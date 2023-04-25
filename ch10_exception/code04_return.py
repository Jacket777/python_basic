"""
测试return语句正确处理方式
"""


def test01():
    print("test01")
    try:
        x = 3 / 0
    except:
        print("step2")
        print("异常：0不能做除数")
        # return "b"
    finally:
        print("step4")
        # return "d"
    print("step5")
    return "e"


if __name__ == '__main__':
    print(test01())
