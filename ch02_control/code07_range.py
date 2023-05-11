# 使用range


def useRangeAndWhile():
    for i in range(5):
        print('Jimmy Five Times ( ' + str(i) + ' ）')
    print("========================")
    i = 0
    while i < 5:
        print('Jimmy Five Times ( ' + str(i) + ' ）')
        i = i + 1


def useRange():
    for i in range(12, 16):
        print(i)
    print('---------------')
    for i in range(0, 10, 2):
        print(i)
    print('-----------------')
    for i in range(5, -1, -1):
        print(i)


def calSum():
    total = 0
    for num in range(101):
        total = total + num
    print(total)


if __name__ == '__main__':
    calSum()

