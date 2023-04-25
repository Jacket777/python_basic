# coding=utf-8
# 测试scale滑块

from tkinter import *

root = Tk()
root.geometry("400x150")

def test1(value):
    print("滑块的值: "+value)
    newFont = ("宋体", value)
    a.config(font=newFont)


s1 = Scale(root, from_=10, to=50, length=200, tickinterval=5, orient=HORIZONTAL, command=test1)
s1.pack()
# from_:开始值， to:最终值，length:宽度， tickinterval :间隔值， orient 水平值

a = Label(root, text="程序员", width=10, height=1, bg="black", fg="white")
a.pack()

root.mainloop()
