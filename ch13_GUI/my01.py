# coding=utf-8
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("我的第一个GUI程序")
root.geometry("500x300+100+200")
btn01 = Button(root)
# 赋值语句前后要空格
btn01["text"] = "点我就送花"
btn01.pack()


# e就是事件对象,函数要和其他区分开，两行区分
# 注释后面要加一个空格
# 逗号后面要加一个空格
def songhua(e):
    messagebox.showinfo("Message", "送你一玫瑰")
    print("送你99朵玫瑰")


btn01.bind("<Button-1>", songhua)


root.mainloop()  # 调用组件的mainloop(),进入事件循环，后面注释要与前面空两行
