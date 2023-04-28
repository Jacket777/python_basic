"""
递归函数的基本原理
"""
def test01(n):
    print("test01",n)
    if(n==0):
        print("over")
    else:
        test01(n-1)
    print("test****",n)

def test02():
    print("test02")


if __name__ == '__main__':
    test01(4)


