#
"""
代码清单02: 字典应用
"""


# 字典应用
def dict_birthday():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    while True:
        print('Enter a name : (blank to quit)')
        name = input()
        if name == '':
            break
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday? ')
            day = input()
            birthdays[name] = day
            print('Birthday database updated')


if __name__ == '__main__':
    dict_birthday()
