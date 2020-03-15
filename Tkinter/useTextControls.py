import datetime
import time
from tkinter import *

# 文本输入和输出相关控件：通常包括：标签（Label）、消息（Message）、输入框（Entry）、文本框（Text）。它们除了前述共同属性外，都具有一些特征属性和功能。
#
# 1.标签（Label）和 消息（Message）：除了单行与多行的不同外，属性和用法基本一致，用于呈现文本信息。
# 值得注意的是：属性text通常用于实例在第一次呈现时的固定文本，而如果需要在程序执行后发生变化，则可以使用下列方法之一实现：
#   a.用控件实例的configure()方法来改变属性text的值，可使显示的文本发生变化；
#   b.先定义一个tkinter的内部类型变量var=StringVar() 的值也可以使显示文本发生变化。

# 例子1：制作一个电子时钟，用root的after()方法每隔1秒time模块以获取系统当前时间，并在标签中显示出来。
#   方法一：利用configure()方法或config()来实现文本变化。
# def getTime():
#     timeStr = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
#     lb.configure(text=timeStr)  # 重新设置标签文本
#     root.after(1000, getTime)  # 每隔1s调用函数 getTime 自身获取时间
#
#
# root = Tk()
# root.title('时钟')
#
# lb = Label(root, text='', fg='blue', font=("黑体", 80))
# lb.pack()
# getTime()
# root.mainloop()

#   方法二：利用textvariable变量属性来实现文本变化。
def getTime():
    var.set(time.strftime("%H:%M:%S"))  # 获取当前时间
    root.after(1000, getTime)  # 每隔1s调用函数 gettime 自身获取时间


root = Tk()
root.title('时钟')
var = StringVar()

lb = Label(root, textvariable=var, fg='blue', font=("黑体", 80))
lb.pack()
getTime()
root.mainloop()

# 2.文本框（Text）
# 常用方法如下：(下表位置的取值可为整数，浮点数或END（末尾），例如0.0表示第0列第0行)
#   方法	                    功能
#   delete(起始位置，[,终止位置])	删除指定区域文本
#   get(起始位置，[,终止位置])	获取指定区域文本
#   insert(位置，[,字符串]...)	将文本插入到指定位置
#   see(位置)	                在指定位置是否可见文本，返回布尔值
#   index(标记)	                返回标记所在的行和列
#   mark_names()	            返回所有标记名称
#   mark_set(标记，位置)	        在指定位置设置标记
#   mark_unset(标记)	        去除标记

# 例子2：每隔1秒获一次当前时间并写入文本框中，
#  方法：调用 datetime.now()获取当前日期时间，用insert()方法每次从文本框txt的尾部（END）开始追加文本。
# def getTime():
#     s = str(datetime.datetime.now()) + '\n'
#     txt.insert(END, s)
#     root.after(1000, getTime)  # 每隔1s调用函数 gettime 自身获取时间
#
#
# root = Tk()
# root.geometry('320x240')
# txt = Text(root)
# txt.pack()
# getTime()
# root.mainloop()

# 3.输入框（Entry）：通常作为功能比较单一的接收单行文本输入的控件，
# 常用方法如下：
# 方法	                    功能
# get()                     取值方法
# delete(起始位置，终止位置)  用于删除文本的（例如：清空输入框为delete(0，END)）
# root = Tk()
# root.geometry('320x240')
# entry = Entry(root)
# entry.pack()
#
#
# def getEntry():
#     var.set(entry.get())
#     root.after(100, getEntry)
#
#
# var = StringVar()
# lb = Label(root, textvariable=var, fg='blue', font=("黑体", 80))
# lb.pack()
# getEntry()
# root.mainloop()
