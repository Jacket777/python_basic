# coding=utf-8
# 测试简单输入框--simpledialog


from tkinter.simpledialog import *

root = Tk()
root.geometry("400x100")


def test1():
    a = askinteger(title="输入你的年龄", prompt="请输入年龄", initialvalue=18, minvalue=1,
                   maxvalue=150)
    # askstring, askfloat使用方法一致
    show["text"] = a


Button(root, text="你多大了？请输入", command=test1).pack()
show = Label(root, width=40, height=3, bg="green")
show.pack()

root.mainloop()
