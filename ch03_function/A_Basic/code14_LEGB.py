#测试LEGB
#第四个str Buildin
#str="global str"  #第三 Global
def outer():
    #str="outer"  #第二 Enclosed
    def inner():
        #str="inner"  #第一Local
        print(str)
    inner()

outer()