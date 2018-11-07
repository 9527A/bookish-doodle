from tkinter import *
import crawler_downloader

downloader = []

def button_download():
    global downloader
    downloader = crawler_downloader.download()
    # t.insert(INSERT, downloader)
    t.insert(INSERT, '爬取完成')

def button_show():
    t.delete(0.0,END)
    t.insert(INSERT, downloader)

window = Tk()
window.title("hello world")
win_s = window.winfo_screenwidth()
win_h = window.winfo_screenheight()
root_s = win_s/2-350
root_h = win_h/2-100
window.geometry('%dx%d+%d+%d' % (root_s,root_h,500,250))#使界面显示位置近似居中

t = Text(window)
t.grid(row=4, column=0, columnspan=2, padx=1, pady=2)

Button(window, text='开始爬取', command=lambda:button_download()).grid(row=3, column=0, sticky=W, pady=3)
Button(window, text='显示数据', command=lambda:button_show()).grid(row=3, column=1, sticky=W, pady=3)

window.mainloop()