from tkinter import *

window = Tk()
window.title("hello world")
win_s = window.winfo_screenwidth()
win_h = window.winfo_screenheight()
root_s = win_s/2-350
root_h = win_h/2-100
window.geometry('%dx%d+%d+%d' % (root_s,root_h,500,250))#使界面显示位置近似居中

Button(window, text='开始爬取').grid(row=3, column=0, sticky=W, pady=3)
Button(window, text='显示数据').grid(row=3, column=1, sticky=W, pady=3)

t = Text(window)
t.insert(1.0, 'hello')
t.grid(row=4, column=0, columnspan=2, padx=1, pady=2)

window.mainloop()