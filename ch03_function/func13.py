#测试lambda表达式，匿名函数
f = lambda a,b,c,d:a*b*c*d
print(f(2,3,4,5))

def test01(a,b,c,d):
    print("======")
    return a*b*c*d

g=[lambda a:a*2,lambda b:b*3]
print(g[0](6))

h=[test01,test01] #函数也是对象
print(h[0](3,4,5,6))