# place布局管理测试
# coding=utf-8
from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("布局管理器palce")
root["bg"] = "white"

f1 = Frame(root, width=200, height=200, bg="green")
f1.palce(x=30, y=30)
Button(root, text="上学堂").place(relx=0.2, x=100, y=20, relwidth=0.2, relheight=0.5)
# 说明：上面按钮先放在父组件的x的0.2中，然后在偏移100
Button(f1, text="程序员").place(relx=0.6, rely=0.7)
Button(f1, text="老师").place(relx=0.5, rely=0.2)
root.mainloop()
