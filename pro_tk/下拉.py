import tkinter
from tkinter import ttk


def templist():
    list1 = ["启动", "停止", "重启"]
    list=list1
    comboxlist["values"] = (list)

def go(*args):  # 处理事件，*args表示可变参数
    print(comboxlist.get())  # 打印选中的值

list=["初始化"]
win = tkinter.Tk()  # 构造窗体
win.title('网关控制小程序')  # 顶层窗口名称
win.geometry("500x300+200+20")  # 设置窗口大小
win.resizable(width=True, height=True)  # 设置窗口是否可变，宽不可变，高可变，默认为True

comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
# num=input(":")
# # list=["启动", "停止", "重启"]
# list.append(num)

# global list=[]
comboxlist["values"] = (list)

comboxlist.current(0)  # 选择第一个
comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)

comboxlist.pack()

btn_save = tkinter.Button(win, text='保存', command=templist)
btn_save.place(x=420, y=15, width=60)
btn_save.pack()

win.mainloop()
