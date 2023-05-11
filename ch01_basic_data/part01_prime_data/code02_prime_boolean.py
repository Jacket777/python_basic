# 布尔值与比较


# 布尔值
def get_boolean_value():
    a = (42 == 42)
    print("42 == 42 ", a)
    a = (42 == 49)
    print("42 == 49 ", a)
    a = (2 != 3)
    print(" 2 != 3 ", a)
    a = (2 != 2)
    print(" 2 != 2 ", a)
    print("=====================")
    a = ('hello' == 'hello')
    print("('hello' == 'hello')", a)
    a = ('hello' == 'Hello')
    print("('hello' == 'Hello')", a)
    a = ('dog' == 'cat')
    print("('dog' == 'cat')", a)
    print("=====================")
    print("(True == True)", (True == True))
    a = (True != False)
    print("(True != False)", a)
    print("========notice=============")
    a = (42 == 42.0)
    print("(42 == 42.0)", a)
    a = (42 == '42.0')
    print("(42 == '42.0')", a)
    a = (42 == 0042.000)
    print("(42 == 0042.000)", a)


#  这四类比较操作符只能应用于整型和浮点型值
#  (>,<,<=,>=)
def compare():
    a = 42 < 100
    print(a)
    b = 42 > 100
    eggCount = 42
    a = eggCount <= 42
    print(a)
    age = 29
    a = age >= 10
    print(a)


#  二元布尔操作符
def boolean_operator():
    a = True and True
    b = True and False
    print("True and True ", a)
    print("True and False ", b)
    a = False or True
    b = False or False
    print("False or True ", a)
    print("False or False ", b)
    a = not True
    b = not not False
    print("not True ", a)
    print("not not False ", b)


#  混合布尔和比较操作符
def complexBoolean():
    a = (4 < 5) and (5 < 6)
    b = (4 < 5) and (9 < 6)
    c = (1 == 2) or (2 == 2)
    d = (2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)
    print(a, b, c, d)


if __name__ == '__main__':
    complexBoolean()



