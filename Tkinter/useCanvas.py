# @Time    : 2020/3/15 21:29
# @Author  : AeishenLin
# @File    : useCanvas.py
# @Describe: 使用Canvas(画布)

# Canvas是tkinter中的画布控件
#   主要属性:
# 属性        意义
# bg        背景色
# fg        前景色
# bitmap    背景位图
# image     底纹图像
# bd        边框宽（像素）
# with      宽度（像素）
# height    高度 (像素)
#   主要绘图方法:
# 方法                功能          主要参数
# creat_arc()        给弧形和扇形 常用的参数除两点位置外，还有start（初始化角度）和 extent（中止角度）。参数fill为填充色，outline 为轮廓线色
# creat_image()      绘图像       用参数file指向图像文件，支持GIF（无动画）、PNG等格式，不支持JPG格式
# creat_line()       绘直线       两点坐标。参数arrow 为箭头样式，默认无，FIRST/LAST分别表示箭头在首/尾。参数dash表示虚线样式的元祖型参数。例 dash(4,2) 表示连续4像素间隔2像素
# create_oval()      绘椭圆       用左上角和右下角两点的位置定位出矩形内切椭圆
# create_polygon()   绘多边形     顶点位置的x和y值作为参数
# create_rectangle() 绘矩形       用左上角和右下角两点的位置定位出矩形
# create_text()      文本标签     显示位置和text(文本内容)
# delete()           删除指定图形  参数为指定图形对象的名称，全部删除为ALL

# --------------------------------------------------------------------------------------
# 1.Canvas创建画布和填充颜色:
# Canvas 画布的坐标原点在左上角，默认单位是像素，x轴向右为正，y轴向下为正。例如：在320x240的窗体上创建高200像素，宽280像素的画布，并填充颜色
# from tkinter import *
#
# root = Tk()
# root.title('绘制图形')
# root.geometry('320x240')
# mycanvas = Canvas(root, bg='green', height=200, width=280)
# mycanvas.pack()
# btn1 = Button(root, text='关闭', command=root.destroy)
# btn1.pack()
# root.mainloop()
# --------------------------------------------------------------------------------------
# 2.Canvas绘制图形:
# 在320x240的窗体上创建高200像素，宽300像素的画布，鼠标点击画布，依次绘出：从(90,10)到(200,200)点的矩形;
# 从(90,10)到(200,200)点的内切椭圆并填充绿色;从(90,10)到(200,200)点的内切扇形并填充粉红色;
# 连接(20,180)、(150,10)和(290,180) 三点形成蓝色框线且无色填充的三角形；从(10,105)到(290,105)点的红色直线；
# 以(50,10)为起点用RGB"#123456"颜色绘制文本标签“我的画布”。单击“清空”按钮删除所有图形，如下：
# from tkinter import *
#
# root = Tk()
# root.title('绘制图形')
# root.geometry('320x240')
#
#
# def delt():
#     mycanvas.delete(ALL)
#
#
# def draw(event):
#     # 画矩形
#     mycanvas.create_rectangle(90, 10, 200, 200)
#     # 画椭圆，填充颜色
#     mycanvas.create_oval(90, 10, 200, 200, fill='green')
#     # 画扇形
#     mycanvas.create_arc(90, 10, 200, 200, fill='pink')
#     # 画多边形（三角形），前景为蓝色，无填充色
#     mycanvas.create_polygon(10, 180, 145, 10, 290, 180, outline='blue', fill='')
#     # 画直线
#     mycanvas.create_line(0, 105, 300, 105, fill='red')
#     # 写文字，颜色为十六进制RGB字符串
#     mycanvas.create_text(50, 10, text='我的画布', fill='#123456')
#
#
# mycanvas: Canvas = Canvas(root, width=300, height=200)
# mycanvas.pack()
# mycanvas.bind('<Button-1>', draw)  # 画布绑定鼠标点击事件
# btnclear = Button(root, text='清空', command=delt)
# btnclear.pack()
#
# root.mainloop()
# --------------------------------------------------------------------------------------
# 3.Canvas呈现位图图像:
# Canvas画布支持呈现位图图像文件，文件的类型包括：GIF(无动画)、PNG等格式，但不支持JPG格式。
# 在320x240的窗体上创建画布，并呈现/Users/wangchong/Desktop/呵呵.png图像
# from tkinter import *
#
# root = Tk()
# root.title('呈现位图图像')
# root.geometry('320x240')
# mycanvas = Canvas(root)
# mycanvas.pack()
# photo = PhotoImage(file='E:/1.png')
# mycanvas.create_image(100, 100, image=photo)
# root.mainloop()
# -------------------------------------------------------------------------------------
# 4.Canvas利用鼠标事件绘图
# 利用鼠标左键移动鼠标事件，不断读取鼠标当前的位置，每次扩张1个像素绘制椭圆点，即可在画布上留下鼠标的轨迹。
# 例如：在320x240的窗体上创建画布，并以红色笔创建鼠标画板。
# 其中，按住鼠标左键移动的鼠标事件<B1-Motion>绑定函数move(event),当按住鼠标左键移动鼠标时，
# 即触发读取鼠标当前位置x=event.x,y=event.y,在点（x,y）与点（x+1,y+1）组成的矩形之间留下蓝色椭圆点。
# from tkinter import *
#
# root = Tk()
#
#
# def move(event):
#     x = event.x
#     y = event.y
#     w.create_oval(x, y, x + 1, y + 1, fill='red')
#
#
# w = Canvas(root, width=320, height=240)
# w.pack()
# w.bind('<B1-Motion>', move)
# root.mainloop()
# -------------------------------------------------------------------------------------
# 5.Canvas函数图形绘制
# 用create_line函数可以在画布上绘制直线，而随着变量的变化，用该方法连续绘制微直线即可得到函数的图形。
# 例如：在窗体上创建320x240的画布，以画布中心为原点，用绿色红色绘制带箭头的x和y坐标轴，用蓝色笔绘制正玄曲线y=sinx的函数图形。
# 其中，x,y轴的放大倍数均为倍数均为40倍，即：x = 40t,t以0.01的步长在 -π~π范围内变化取值。
from tkinter import *
import math

root = Tk()
w = Canvas(root, width=320, height=240)
w.pack()
w0 = 160  # 半宽
h0 = 120  # 半高
# 画红色的坐标轴线
w.create_line(0, 120, 320, 120, fill="green", arrow=LAST)
w.create_line(160, 240, 160, 0, fill="red", arrow=LAST)
# 标题文字
w.create_text(w0 + 50, 10, text='y=sin(x)')
# x轴刻度
for i in range(-3, 4):
    j = i * 40
    w.create_line(j + w0, h0, j + w0, h0 - 5, fill="red")
    w.create_text(j + w0, h0 + 5, text=str(i))
# y轴刻度
for i in range(-2, 3):
    j = i * 40
    w.create_line(w0, j + h0, w0 + 5, j + h0, fill="red")
    w.create_text(w0 - 10, j + h0, text=str(-i))


# 计算x
def x(t_):
    x_ = t_ * 40  # x轴放大40倍
    x_ += w0  # 平移x轴
    return x_


# 计算y
def y(t_):
    y_ = math.sin(t_) * 40  # y轴放大40倍
    y_ -= h0  # 平移y轴
    y_ = -y_  # y轴值反向
    return y_


# 连续绘制微置线
t = -math.pi
while t < math.pi:
    w.create_line(x(t), y(t), x(t + 0.01), y(t + 0.01), fill="blue")
    t += 0.01
root.mainloop()
