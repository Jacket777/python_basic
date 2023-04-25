"""测试布局管理器--grid实现计算器页面"""
# coding=utf8
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        """通过grid布局实现计算器页面"""
        # 按键文本
        btnText = (("MC", "M+", "M-", "MR"),
                   ("C", "±", "/", "*"),
                   ("7", "8", "9", "-"),
                   ("4", "5", "6", "+"),
                   ("1", "2", "3", "="),
                   ("0", ".")
                   )
        # 输入框
        Entry(self).grid(row=0, column=0, columnspan=4,pady=10)
        # 遍历文本，生成按键
        for rindex, r in enumerate(btnText):
            for cindex,c in enumerate(r):
                if c == "=":
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex, rowspan=2, sticky=NSEW)
                elif c == "0":
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex, columnspan=2, sticky=NSEW)
                elif c == ".":
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex+1, sticky=EW)
                else:
                    Button(self, text=c, width=2) \
                        .grid(row=rindex + 1, column=cindex, sticky=EW)




if __name__ == "__main__":
    root = Tk()
    root.geometry("300x300+200+300")
    app = Application(master=root)
    root.mainloop()
