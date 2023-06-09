# coding=utf-8
# 测试pack布局管理器--面向对象

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.frame01 = Frame(self)
        self.frame01.pack()
        self.frame02 = Frame(self)
        self.frame02.pack()
        btnText = ("流行风", "中国风", "日本风", "重金属", "轻音乐")
        for txt in btnText:
            Button(self.frame01, text=txt).pack(side="left", padx="10")

        for i in range(1, 20):
            Label(self.frame02, width=5, height=10, borderwidth=1, relief="solid",
                  bg="black" if i % 2 == 0 else "white").pack(side="left", padx=2)



if __name__ =="__main__":
    root = Tk()
    root.geometry("700x220")
    app = Application(master=root)
    root.mainloop()







