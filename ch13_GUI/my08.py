"""测试多选按钮--CheckButton"""
# coding=utf8
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.codeHobby = IntVar()
        self.vidoeHobby = IntVar()
        print(self.codeHobby.get()) # 默认值为0
        self.c1 = Checkbutton(self,text="敲代码",
                              variable=self.codeHobby, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(self,text="看视频",
                              variable=self.vidoeHobby, onvalue=1, offvalue=0)
        self.c1.pack(side="left")
        self.c2.pack(side="left")
        Button(self, text="确定", command=self.confirm).pack(side="left")

    def confirm(self):
        if self.vidoeHobby.get() == 1:
            messagebox.showinfo("测试", "看视频")
        if self.codeHobby.get() == 1:
            messagebox.showinfo("测试", "敲代码")







if __name__ == "__main__":
    root = Tk()
    root.geometry("400x250+200+300")
    app = Application(master=root)
    root.mainloop()