# coding=utf-8
# 测试Optionmenu的选项菜单测试

from tkinter import *

root = Tk()
root.geometry("200x100")
v = StringVar(root)
v.set("程序员")
om = OptionMenu(root, v, "大学堂", "程序员", "超越")
om["width"] = 10
om.pack()


def test1():
    print("最喜欢的机构: " + v.get())
    # v.set("大学堂") #直接修改了optionmenu选中的值


Button(root, text="确定", command=test1).pack()

root.mainloop()