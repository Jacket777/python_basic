# 控制流
import sys


def testIf():
    print('Input your name')
    name = input()
    print('Input your age')
    age = input()
    age = int(age)
    if name == 'Alice':
        print('Hi,Alice')
    elif age < 12:
        print('You are not Alice, Kiddo')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire')
    elif age > 100:
        print('You are not Alice, grannie')


def testWhile():
    spam = 0
    while spam < 5:
        print('Hello world')
        spam = spam + 1


def testName():
    name = ''
    while name != 'your name':
        print('please type your name.')
        name = input()
    print('Thank you!')


def testBreak():
    while True:
        print('Please type your name.')
        name = input()
        if name == 'your name':
            break;
    print('Thank you!')


def testContinue():
    while True:
        print("who are you ?")
        name = input()
        if name != 'joe':
            continue
        print('Hello, Joe, What is the password ? (It is  a fish)')
        password = input()
        if password == 'swordfish':
            break
    print("Access granted. ")


# 空字符串，0,0.0被认为为False其他值为True
def testNullStr():
    name = ''
    while not name:
        print('Enter your name: ')
        name = input()
        print('How many guests will you have?')
        numOfGuests = int(input())
        if numOfGuests:
            print('Be sure to have enought room for all your guests')
        print('Done')


# 退出程序
def exitSys():
    while True:
        print('Type exit to exit system. ')
        response = input()
        if response == 'exit':
            sys.exit()
        print('You typed ' + response + '.')


if __name__ == '__main__':
    exitSys()
