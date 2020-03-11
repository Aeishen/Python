# 按钮(Button)：主要是为响应鼠标单击事件触发运行程序所设的，故其除控件共有属性外，属性command是最为重要的属性。
# 通常，将按钮要触发执行的程序以函数形式预先定义，然后可以用一下两种方法调用函数。Button按钮的状态有：'normal','active','disabled'
#   1.直接调用函数。参数表达式为“command=函数名”，注意函数名后面不要加括号，也不能传递参数。如下面的command=run1：
#   2.利用匿名函数调用函数和传递参数。参数的表达式为“command=lambda”:函数名（参数列表）。例如下面的："command=lambda:run2(inp1.get(),inp2.get())"。

# 例子1：
#   1.从两个输入框去的输入文本后转为浮点数值进行加法运算，要求每次单击按钮产生的算是结果以文本的形式追加到文本框中，将原输入框清空。
#   2.按钮方法一不传参数调用函数run1()实现，按钮“方法二”用lambda调用函数run2(x,y)同时传递参数实现。
from tkinter import *

root = Tk()
root.title("计算机")
root.geometry('480x480')
resultVar = StringVar()


def calWithParam(param1, symbolVar, param2):
    value = 0
    if symbolVar == "+":
        value = float(param1) + float(param2)
    elif symbolVar == "-":
        value = float(param1) - float(param2)
    elif symbolVar == "*":
        value = float(param1) * float(param2)
    elif symbolVar == "/":
        if float(param2) == 0:
            resultVar.set("请输入正确除数")
            paramEntry2.delete(0, END)
            return
        else:
            value = float(param1) / float(param2)
    else:
        resultVar.set("请输入正确符号")
        return

    resultVar.set('%0.2f%0.2s%0.2f=%0.2f\n' % (param1, symbolVar, param2, value))
    paramEntry1.delete(0, END)
    paramEntry2.delete(0, END)
    symbolEntry.delete(0, END)


def calWithoutParam():
    value = 0
    symbolVar = symbolEntry.get()
    param1 = float(paramEntry1.get())
    param2 = float(paramEntry2.get())
    if symbolVar == "+":
        value = param1 + param2
    elif symbolVar == "-":
        value = param1 - param2
    elif symbolVar == "*":
        value = param1 * param2
    elif symbolVar == "/":
        if param2 == 0:
            resultVar.set("请输入正确除数")
            paramEntry2.delete(0, END)
            return
        else:
            value = param1 / param2
    else:
        resultVar.set("请输入正确符号")
        return

    resultVar.set('%0.2f%0.2s%0.2f=%0.2f\n' % (param1, symbolVar, param2, value))
    paramEntry1.delete(0, END)
    paramEntry2.delete(0, END)
    symbolEntry.delete(0, END)


tips = Label(root, text="请输入两个数，以及一个符号，按下面两个按钮之一进行计算", height=3)
tips.pack()


paramEntry1 = Entry(root)
paramEntry1 .place(x=80, y=80, relheight=0.08, width=100)
symbolEntry = Entry(root)
symbolEntry.place(x=210, y=80, relheight=0.08, width=60)
paramEntry2 = Entry(root)
paramEntry2.place(x=300, y=80, relheight=0.08, width=100)
funcButton1 = Button(root, text="没参数方法", command=calWithoutParam)
funcButton1.place(x=80, y=160, relheight=0.1, width=80)
funcButton2 = Button(root, text="有参数方法", command=lambda: calWithParam(paramEntry1.get(), symbolEntry.get(), paramEntry2.get()))
funcButton2.place(x=320, y=160, relheight=0.1, width=80)
resultLabel = Label(root, textvariable=resultVar, height=3)
resultLabel.place(relx=0.4, y=240, relheight=0.1, width=120)

root.mainloop()



