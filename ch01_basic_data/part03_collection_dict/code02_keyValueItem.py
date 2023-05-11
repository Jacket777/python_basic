"""
字典 键 值 元素的使用
"""
import pprint


# 1. 字典key-value- item使用
def dict_key_value():
    spam = {'color': 'red', 'age': 42}
    print('=====获取字典的键======')
    # TODO 1 获取字典key的值
    keys = spam.keys()  # 类dict_keys对象
    print(type(keys))  # 类型为 dict_keys
    print(keys)  # dict_keys(['color', 'age'])
    for k in keys:
        print(k, type(k))
    # TODO 2 获取字典value的值
    print("=======获取字典的的值========")
    values = spam.values()
    print(values)
    print(type(values))
    for v in values:
        print(v)
    # TODO 3 获取字典item的值
    print("=======获取字典的的item的值========")
    items = spam.items()  # 获得是dict_item类对象
    print(type(items))  # 类型为dict_items
    print(items)  # 输出为dict_items([('color', 'red'), ('age', 42)])
    for i in items:
        print(i)  # 返回的是元祖  i的类型为元组
    for k, v in items:
        print('key: ' + k + ' value: ' + str(v))


# 2. 字典的key-value-item检查
def dict_check():
    spam = {'name': 'Zophie', 'age': 7}
    print('name' in spam.keys())  # 检查键是否存在
    print('Zophie' in spam.values())  # 检查值是否存在
    print('color' in spam.keys())  # 检查键是否存在
    print('color' not in spam.keys())
    print('color' in spam)
    print('age' in spam)  # 检查键是否存在
    print('Zophie' in spam)


# 3. 获取键值对时，防止异常，设置默认值 get  picnic 野餐
def dict_get():
    picnicItems = {'apple': 5, 'cups': 2}
    # TODO 1. 字典中该键值对存在，则正常获取，如果不存在，则获取默认值
    result = 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
    print(result)
    result2 = 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
    print(result2)


# 4. 设置默认值
def dict_set_default():
    spam = {'name': 'Pooka', 'age': 5}
    print(spam)
    # TODO 1. 第一次设置默认值有效
    spam.setdefault('color', 'black')
    print(spam)
    # TODO 1. 第二次设置默认值无效
    spam.setdefault('color', 'white')
    print(spam['color'])


# 5. 实际案例--字母统计
def character_count():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    pprint.pprint(count)


if __name__ == '__main__':
    # dict_key_value()
    # dict_check()
    # dict_get()
    # dict_set_default()
    character_count()
