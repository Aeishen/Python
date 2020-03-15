# @Time    : 2020/3/15 13:20
# @Author  : AeishenLin
# @File    : useCombobox.py
# @Describe: 使用列表框

# 列表框：(Listbox) 可供用户单选或多选所列条目以形成人机交互。
#   列表框控件的主要方法:
#       方法                        功能描述
#       curselection()              返回光标选中项目编号的元组，注意并不是单个的整数
#       delete(起始位置，终止位置)    删除项目，终止位置可省略，全部清空为delete(0,END)
#       get(起始位置，终止位)         返回范围所含项目文本的元组，终止位置可忽略
#       insert(位置，项目元素)       插入项目元素（若有多项，可用列表或元组类型赋值），若位置为END，则将项目元素添加在最后
#       size()                      返回列表框行数
#
# 执行自定义函数时，通常使用“实例名.surselection()” 或 “selected” 来获取选中项的位置索引。
# 由于列表框实质上就是将Python 的列表类型数据可视化呈现，在程序实现时，也可直接对相关列表数据进行操作，
# 然后再通过列表框展示出来，而不必拘泥于可视化控件的方法。
# 看下面的一个例子：实现列表框的初始化、添加、插入、修改、删除和清空操作，如下：
from tkinter import *

root = Tk()
root.title('列表框使用')
root.geometry('320x320')


def initLstBox1():
    LstBox1.delete(0, END)
    listItems = ["数学", "物理", "化学", "语文", "外语"]
    for item in listItems:
        LstBox1.insert(END, item)


def clearLstBox1():
    LstBox1.delete(0, END)


def insertLstBox1():
    if entry.get() != '':
        if LstBox1.curselection() == ():
            LstBox1.insert(LstBox1.size(), entry.get())
        else:
            LstBox1.insert(LstBox1.curselection(), entry.get())


def updateLstBox1():
    if entry.get() != '' and LstBox1.curselection() != ():
        selected = LstBox1.curselection()[0]
        LstBox1.delete(selected)
        LstBox1.insert(selected, entry.get())


def deleteLstBox1():
    if LstBox1.curselection() != ():
        LstBox1.delete(Lstbox1.curselection())


frame1 = Frame(root, relief=RAISED)
frame1.place(relx=0.0)

frame2 = Frame(root, relief=GROOVE)
frame2.place(relx=0.5)

LstBox1 = Listbox(frame1)
LstBox1.pack()

entry = Entry(frame2)
entry.pack()

btn1 = Button(frame2, text='初始化', command=initLstBox1)
btn1.pack(fill=X)

btn2 = Button(frame2, text='添加', command=insertLstBox1)
btn2.pack(fill=X)

btn3 = Button(frame2, text='插入', command=insertLstBox1)  # 添加和插入功能实质上是一样的
btn3.pack(fill=X)

btn4 = Button(frame2, text='修改', command=updateLstBox1)
btn4.pack(fill=X)

btn5 = Button(frame2, text='删除', command=deleteLstBox1)
btn5.pack(fill=X)

btn6 = Button(frame2, text='清空', command=clearLstBox1)
btn6.pack(fill=X)

root.mainloop()
