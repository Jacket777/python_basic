# coding=utf-8
# 测试通用消息框-simpledialog

from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.geometry("400x100")


a1 = showinfo(title="消息框", message="测试")
print(a1)

root.mainloop()
