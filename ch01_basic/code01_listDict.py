
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
	test01()



