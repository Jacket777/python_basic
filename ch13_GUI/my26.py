# coding=utf-8
# 测试菜单

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建主菜单
        menubar = Menu(root)

        # 创建子菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        #  将子菜单加入到主菜单栏
        menubar.add_cascade(label="文件(F)", menu=menuFile)
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="帮助(H)", menu=menuHelp)

        # 添加菜单项
        menuFile.add_command(label="新建", accelerator="ctr+n", command=self.test)
        menuFile.add_command(label="打开", accelerator="ctr+o", command=self.test)
        menuFile.add_command(label="保存", accelerator="ctr+s", command=self.test)
        menuFile.add_separator()
        menuFile.add_command(label="退出", accelerator="ctr+q", command=self.test)

        # 将主菜单栏加到根窗口
        root["menu"] = menubar

        # 文本编辑区
        self.textpad = Text(root, width=50, height=30)
        self.textpad.pack()

        # 创建上下菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="背景颜色", command=self.test)

        # 为右键绑定事件
        root.bind("<Button-3>", self.createContextMenu)

    def test(self):
        pass

    def createContextMenu(self, event):
        # 菜单在鼠标右键单击的坐标处显示
        self.contextMenu.post(event.x_root, event.y_root)


if __name__ == "__main__":
    root = Tk()
    root.geometry("450x300+200+300")
    app = Application(master=root)
    root.mainloop()
