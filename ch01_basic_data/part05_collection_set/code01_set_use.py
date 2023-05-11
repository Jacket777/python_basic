# 集合（set使用）运算


def set_calculator():
    # TODO 01 集合的定义
    basket = {'apple', 'orange', 'apple', 'peer', 'orange', 'banana'}
    print(basket)  # 重复添加的数据只会被添加一次
    result = 'orange' in basket  # 检查元素是否在集合中，返回Boolean值
    print(result)
    result = 'crabgrass' in basket
    print(result)
    a = set('apple')  # 以字符的形式存放在集合中,p有两个，但只存一个p
    print(a)
    b = set('abandon')
    print(b)
    c = a - b  # 去除a集合与b集合中共有的元素，留下a中剩余的元素
    print(c)
    d = a | b  # 集合a,b所有的元素，重复的必须删除
    print(d)
    e = a & b  # 集合a,b都包含的元素
    print(e)
    f = a ^ b  # 集合a,b所有的元素，去除a, b公有的元素
    print(f)
    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)  # x 不属于a,b,c 的集合


if __name__ == '__main__':
    set_calculator()



