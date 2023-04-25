# 测试text组件
# coding=utf-8

from tkinter import *
from tkinter import messagebox
import webbrowser


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.w2 = Text(root, width=40, height=12, bg="gray")
        # 宽度20个字母（10个汉字），高度一个行高
        self.w2.pack()
        self.w2.insert(1.0, "0123456789\nabcdefg")
        self.w2.insert(2.3, "锄禾日当午, 汗滴禾下土。谁知盘中餐,粒粒皆辛苦\n")

        Button(self, text="重复插入文本", command=self.insertText).pack(side="left")
        Button(self, text="返回文本", command=self.returnText).pack(side="left")
        Button(self, text="添加图片", command=self.addImage).pack(side="left")
        Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        Button(self, text="通过tag精确控制文本", command=self.testTage).pack(side="left")

    def insertText(self):
        # INSERT索引表示在光标处插入
        self.w2.insert(INSERT, ' gaoqi ')
        # END索引号表示在最后插入
        self.w2.insert(END, '[sxt]')

    def returnText(self):
        # Indexs索引使用来指向Text组件中文本的位置，Text组件索引也是对应实际字符之间的位置
        # 核心： 行号以1开始，列号以0开始
        print(self.w2.get(1.2, 1.6))
        print("所有文本内容: \n"+self.w2.get(1.0,END))

    def addImage(self):
        self.photo = PhotoImage(file="imgs/logo.gif")
        self.w2.image_create(END,image=self.photo)

    def addWidget(self):
        b1 = Button(self.w2, text="大学堂")
        # 在text创建组件的命令
        self.w2.window_create(INSERT, window=b1)

    def testTage(self):
        self.w2.delete(1.0,END)
        self.w2.insert(INSERT,"good good study,day day up!\n北京大学堂\n百战程序员\n百度，搜一下")
        self.w2.tag_add("good", 1.0, 1.9)
        self.w2.tag_config("good", background="yellow", foreground="red")

        self.w2.tag_add("baidu", 4.0, 4.2)
        self.w2.tag_config("baidu", underline=True)
        self.w2.tag_bind("baidu","<Button-1>",self.webshow)

    def webshow(self, event):
        webbrowser.open("http://www.baidu.com")



if __name__ == "__main__":
    root = Tk()
    root.geometry("400x250+200+300")
    app = Application(master=root)
    root.mainloop()