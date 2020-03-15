# @Time    : 2020/3/15 16:13
# @Author  : AeishenLin
# @File    : useModalDialogBox.py
# @Describe: 使用模式对话框

# 是相对于其他非模式窗体而言的，所弹出的对话框必须应答，在关闭之前无法操作其后面的其他窗体。
# 常见的模式对话框有消息对话框、输入对话框、文件选择对话框、颜色选择对话框等。

# (一)、交互对话框
# 1.消息对话框: 引用 tkinter.messagebox 包，可使用消息对话框函数。执行这些函数，可弹出模式消息对话框，并根据用户的响应但会一个布尔值。
# 其通式为：消息对话框函数(<title=标题文本>,<message=消息文本>,[其他参数])
# 看下面的例子：单击按钮，弹出确认取消对话框，并将用户回答显示在标签中。
# from tkinter import *
# import tkinter.messagebox
#
#
# def pop():
#     answer = tkinter.messagebox.askokcancel('请选择', '请选择确定或取消')
#     if answer:
#         lb.config(text='已确认')
#     else:
#         lb.config(text='已取消')
#
#
# root = Tk()
# root.title('消息对话框')
# root.geometry('320x320')
# lb = Label(root, text='')
# lb.pack()
# btn = Button(root, text='弹出对话框', command=pop)
# btn.pack()
# root.mainloop()


# 2.输入对话框: 引用tkinter.simpledialog包，可弹出输入对话框，用以接收用户的简单输入。
# 输入对话框常用 askstring()、askfloat()和askfloat() 三种函数，分别用于接收字符串、整数和浮点数类型的输入。
# 如下面的例子：单击按钮，弹出输入对话框，接收文本输入显示在窗体的标签上。如下：
# from tkinter import *
# import tkinter.simpledialog
#
#
# def pop():
#     str = tkinter.simpledialog.askstring('请输入', '请输入一串文字')
#     if str != '':
#         lb.config(text=str)
#
#
# root = Tk()
# root.title('输入对话框')
# root.geometry('320x320')
# lb = Label(root, text='')
# lb.pack()
# btn = Button(root, text='弹出对话框', command=pop)
# btn.pack()
# root.mainloop()


# (二)、文件选择对话框：引用tkinter.filedialog包，可弹出文件选择对话框，让用户直观地选择一个或一组文件，以供进一步的文件操作。
# 常用的文件选择对话框函数有 askopenfilename()、askopenfilenames()和asksaveasfilename(),分别用于进一步打开一个文件、一组文件和保存文件。
# 其中，askopenfilename()和asksaveasfilenamme()函数的返回值类型为包含文件路径的文件名字符串，而askopenfilenames()函数的返回值类型为元组。
# 例如：单击按钮，弹出文件选择对话框（“打开”对话框），并将用户所选择的文件路径和文件名显示在窗体的标签上:
# from tkinter import *
# import tkinter.filedialog
#
#
# def pop():
#     filename = tkinter.filedialog.askopenfilename()
#     if filename != '':
#         lb.config(text='您选择的文件是' + filename)
#     else:
#         lb.config(text='您没有选择任何文件')
#
#
# root = Tk()
# root.title('文件选择对话框')
# root.geometry('320x320')
# lb = Label(root, text='')
# lb.pack()
# btn = Button(root, text='弹出文件选择对话框', command=pop)
# btn.pack()
# root.mainloop()


# (三)、颜色选择对话框：引用tkinter.colorchooser包，可使用 askcolor()函数弹出模式颜色选择对话框，让用户可以个性化地设置颜色属性。
# 该函数的返回形式为包含RGB十进制浮点元组和RGB十六进制字符串的元组类型，
# 例如：“((135.527343.52734375,167.65234375,186.7265625)),'#87a7ba'”。
# 通常，可将其转换为字符串类型后，再截取以十六进制数表示的RGB颜色字符串用于为属性赋值。
# 举例：单击按钮，弹出颜色选择对话框，并将用户所选择的颜色设置为窗体上标签的背景颜色，
from tkinter import *
import tkinter.colorchooser


def pop():
    color = tkinter.colorchooser.askcolor()
    colorstr = str(color)
    print('打印字符串%s 切掉后=%s' % (colorstr, colorstr[-9:-2]))
    lb.config(text=colorstr[-9:-2], background=colorstr[-9:-2])


root = Tk()
root.title('颜色选择对话框')
root.geometry('320x320')
lb = Label(root, text='请关注颜色的变化')
lb.pack()
btn = Button(root, text='弹出颜色选择对话框', command=pop)
btn.pack()
root.mainloop()
