"""
代码清单01 字典的基本使用
"""


# TODO 1. 字典定义与使用
def dict_use():
    myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}  # 字典的定义
    print(myCat['size'])  # 字典的获取值
    print(myCat)
    str01 = 'My cat has ' + myCat['color'] + ' fur.'
    print(str01)


# TODO 2. 字典与列表比较不同
def dict_list():
    spam = ['cats', 'dogs', 'moose']
    bacon = ['dogs', 'moose', 'cats']
    print(spam == bacon)  # 列表必须有序
    eggs = {'name': 'Zophie', 'species': 'cat', 'egg': '8'}
    ham = {'species': 'cat', 'name': 'Zophie', 'egg': '8'}
    print(eggs == ham)  # 字典无序


# TODO 3. 字典的生成
def dict_gen():
    # 1. 使用dict 将列表转为字典
    dict01 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(dict01)
    # 2. 使用字典推导式
    dict02 = {x: x ** 2 for x in (2, 4, 6)}
    print(dict02)
    # 3. 使用dict特别
    dict03 = dict(spae=4139, guido=4127, jack=4098)
    print(dict03)


def test02():
	r1 = {"name": "高小一", "age": 18, "salary": 3000, "city": "北京"}
	r2 = {"name": "高小二", "age": 19, "salary": 2000, "city": "上海"}
	r3 = {"name": "高小三", "age": 19, "salary": 1000, "city": "深圳"}
	tb = [r1, r2, r3]

	# 获取第二行的人的薪资
	b = tb[1].get("salary")
	print(b)

	# 打印所有人的薪资
	for i in range(len(tb)):  # i-->0,1,2
		print(tb[i].get("salary"))

	# 打印表中所有数据
	for i in range(len(tb)):
		print(tb[i].get("name"), tb[i].get("age"), tb[i].get("salary"), tb[i].get("city"))


if __name__ == '__main__':
    dict_list()
