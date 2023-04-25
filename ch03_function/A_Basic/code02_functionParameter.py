# 测试形参和实参的基本用法

def printMax(a, b):
    '''比较两个值的大小'''
    if a > b:
        print(a, "较大值")
    else:
        print(b, "较大值")


printMax(10, 20)
printMax(200, 300)
help(printMax.__doc__)
