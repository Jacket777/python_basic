# 使用集合与不使用集合比较


# 不使用集合
def use_not_collection():
    print('Enter the name of cat 1: ')
    catName1 = input()
    print('Enter the name of cat 2: ')
    catName2 = input()
    print('Enter the name of cat 3: ')
    catName3 = input()
    print('Enter the name of cat 4: ')
    catName4 = input()
    print('Enter the name of cat 5: ')
    catName5 = input()
    print('Enter the name of cat 6: ')
    catName6 = input()
    print('The cat name are: ')
    print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' + catName5 + ' ' + catName6)


#  使用集合
def use_collection():
    catNames = []
    while True:
        print('Enter the name of cat ' + str(len(catNames) + 1) + '(Or enter nothing to stop.): ')
        name = input()
        if name == '':
            break
        catNames = catNames + [name]
    print('The cat names are: ')
    for name in catNames:
        print(' ' + name)


def test01():
    a = [
        ["gao", 18, 900, "beijing"],
        ["jack", 21, 800, "nanjing"],
        ["tom", 22, 700, "nantong"]
    ]
    for m in range(3):
        for n in range(4):
            print(a[m][n], end="\t")
        print()


if __name__ == '__main__':
    use_not_collection()
