"""
list简单应用
"""
import random
from collections import deque


# 1 随机生成答案
def random_answer():
    messages = ['It is certain',
                'It is decidedly so',
                'Yes definitely',
                'Reply hazy try again',
                'Ask again later',
                'Concentrate and ask again',
                'My reply is no',
                'Outlook not so good',
                'Very doubtful',
                ]
    print(messages[random.randint(0, len(messages) - 1)])


# 检查列表元素
def pet_list():
    myPets = ['Zophie', 'Pooka', 'Fat-tail']
    print('Enter a pet name: ')
    name = input()
    if name not in myPets:
        print('I do not have a pet named ' + name)
    else:
        print(name + ' is my pet.')


# 列表转为栈
def list_as_stack():
    stack = [3, 4, 5, 6, 7]
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)


#  4 列表转为队列
def list_as_queue():
    queue = deque(['Eric', 'John', 'Michael'])
    queue.append('Terry')
    queue.append('Graham')
    item01 = queue.popleft()
    print(item01)
    item02 = queue.pop()
    print(item02)


if __name__ == '__main__':
    random_answer()
