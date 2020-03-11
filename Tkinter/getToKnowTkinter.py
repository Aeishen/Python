from tkinter import  *

# 根窗口
root = Tk()  # 根窗体是图像化应用程序的根控制器，是tkinter的底层控件的实例。当导入tkinter模块后，调用 Tk()方法可初始化一个根窗体实例 root
root.title("68")  # 设置其标题文字
root.geometry('320x240')  # 设置窗体的大小（以像素为单位）

# 常用控件：
# 控件	        名称	    作用
# Button	    按钮	    单击触发事件
# Canvas	    画布	    绘制图形或绘制特殊控件
# Checkbutton	复选框	    多项选择
# Entry  	    输入框	    接收单行文本输入
# Frame	        框架	    用于控件分组
# Label	        标签	    单行文本显示
# Lisbox	    列表框	    显示文本列表
# Menu	        菜单	    创建菜单命令
# Message	    消息	    多行文本标签，与Label 用法类似
# Radiobutton	单选按钮	    从互斥的多个选项中做单项选择
# Scale	        滑块	    默认垂直方向，鼠标拖动改变数值形成可视化交互
# Scrollbar	    滑动条	    默认垂直方向，课鼠标拖动改变数值，可与 Text、Lisbox、Canvas等控件配合移动可视化空间
# Text	        文本框	    接收或输出显示多行文本
# Toplevel	    新建窗体容器	在顶层创建新窗体


# 控件的共同属性
# 属性	    说明	                        取值
# anchor	文本起始位置	                    CENTER(默认)，E,S,W,N,NE,SE,SW,NW
# bg	    背景色	                        无
# bd	    加粗（默认2像素）	                无
# bitmap	黑白二值图标	                    网上查找
# cursor	鼠标悬停光标	                    网上查找
# font	    字体	                        无
# fg	    前景色	                        无
# height	高（文本控件的单位为行，不是像素）	无
# image	    显示图像	                        无
# justify	多行文本的对其方式	            CENTER(默认)，LEFT,RIGHT,TOP,BOTTOM
# padx	    水平扩展像素	                    无
# pady	    垂直扩展像素	                    无
# relief	3D浮雕样式	                    FLAT,RAISED,SUNKEN,GROOVE,RIDGE
# state	    控件实例状态是否可用	            NORMAL(默认)，DISABLED
# width	    宽(文本控件的单位为行,不是像素)	无


# 控件布局
# 1.pack()方法：简单的布局，如果不加参数的默认方式，将按布局语句的先后，以最小占用空间的方式自上而下地排列控件实例，并且保持控件本身的最小尺寸。
#   常用布局参数如下：
#       fill 可取值：fill=X,fill=Y或fill=BOTH，分别表示允许控件向水平方向、垂直方向或二维伸展填充未被占用控件。
#       side 可取值：side=TOP(默认)，side=LEFT,side=RIGHT,side=BOTTOM,分别表示本控件实例的布局相对于下一个控件实例的方位。
#
# 2.grid()方法：基于网格的布局。先虚拟一个二维表格，再在表格中布局控件实例。由于在虚拟表格的单元中所布局的控件实例大小不一，单元格也没有固定或均一的大小，因此其仅用于布局的定位。
#   常用布局参数如下：（pack()方法与grid()方法不能混合使用。）
#       column: 控件实例的起始列，最左边为第0列。
#       columnspan: 控件实例所跨越的列数，默认为1列。
#       ipadx,ipady: 控件实例所呈现区域内部的像素数，用来设置控件实例的大小。
#       padx,pady: 控件实例所占据空间像素数，用来设置实例所在单元格的大小。
#       row: 控件实例的起始行，最上面为第0行。
#       rowspan: 控件实例的起始行数，默认为1行。
#
# 3.place()方法：根据控件实例在父容器中的绝对或相对位置参数进行布局。
#   其常用布局参数如下：（place()方法与grid()方法可以混合使用）
#       x,y：控件实例在根窗体中水平和垂直方向上的其实位置（单位为像素）。注意，根窗体左上角为0,0,水平向右，垂直向下为正方向。
#       relx,rely：控件实例在根窗体中水平和垂直方向上起始布局的相对位置。即相对于根窗体宽和高的比例位置，取值在0.0~1.0之间。
#       height,width：控件实例本身的高度和宽度（单位为像素）。
#       relheight,relwidth：控件实例相对于根窗体的高度和宽度比例，取值在0.0~1.0之间。
#       利用place()方法配合relx,rely和relheight,relwidth参数所得的到的界面可自适应根窗体尺寸的大小。


# but = Button(root, width=10, height=2, text="按钮")
# but.pack()
# labRed = Label(root, text="凹陷的", bg='#d3fbfb', fg='red', font=('微软雅黑', 32), relief=SUNKEN)
# labRed.pack(side=RIGHT)
# labBlue = Label(root, text="凸起的", bg='#d3fbfb', fg='blue', font=('微软雅黑', 32), relief=RAISED)
# labBlue.pack(fill=X)

labRed = Label(root, text="红色", fg="Red", relief=GROOVE)
labRed.grid(column=2, row=0)
labGreen = Label(root, text="绿色", fg="green", relief=GROOVE)
labGreen.grid(column=0, row=1)
labBlue = Label(root, text="蓝色", fg="blue", relief=GROOVE)
labBlue.grid(column=1, columnspan=2, ipadx=20, row=2)
msg1 = Message(root, text='''我的水平起始位置相对窗体 0.2，垂直起始位置为绝对位置 80 像素，我的高度是窗体高度的0.5，宽度是200像素''', relief=GROOVE)
msg1.place(relx=0.2, y=80, relheight=0.5, width=200)
root.mainloop()  # 置于主循环中，除非用户关闭，否则程序始终处于运行状态
