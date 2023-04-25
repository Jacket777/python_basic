# coding=utf-8
# 测试文件选择框--读取文件内容

from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry("400x100")


def test1():
    with askopenfile(title="上传文件",
                     initialdir="c:", filetypes=[("文本文件", ".txt")]) as f:
        # print(f)
        show["text"] = f.read()


Button(root, text="选读取的文件", command=test1).pack()
show = Label(root, width=40, height=3, bg="green")
show.pack()

root.mainloop()
