from tkinter import *
# from tkinter import ttk
from tkinter import scrolledtext
import crawler_downloader
from PIL import Image,ImageTk
import tkinter.messagebox as messagebox
import crawler_mongo
import requests
import os

downloader = []

def button_download():
    # t.delete(0.0,END)
    # global downloader
    # number = crawler_downloader.download()
    # # t.insert(INSERT, downloader)
    # t.insert(INSERT, '爬取完成\n')
    # t.insert(INSERT,'共取得'+str(number)+'页')
    win_download = Toplevel(window)
    win_download.title('爬虫')

    def hitBegin():
        if page.get() == '':
            messagebox.showerror(title='错误', message='请输入要爬取的页数')
        else:
            crawler_downloader.download(int(page.get()))
            t.insert(INSERT, '爬取完成\n')
            t.insert(INSERT,'共取得'+str(page.get())+'页')
            win_download.destroy()

    page = StringVar()
    Label(win_download, text='要爬取的页数:').grid(row=0, column=0)
    Entry(win_download, textvariable=page).grid(row=1, column=0)
    Button(win_download, text='开始', command=hitBegin).grid(row=1, column=1)
    Text(win_download, width=30, height=7).grid(row=2, column=0 ,columnspan=2)

def button_show():
    t.delete(0.0,END)
    data = crawler_mongo.data_get()
    for d in data:
        data_name=d['name']
        data_src=d['src']
        data_intro = d['intro']
        t.insert(INSERT, data_name)
        t.insert(INSERT, data_intro+'\n')
        t.insert(INSERT, data_src)
    
def button_img(k):
    global Photo

    t.delete(0.0,END)
    data = crawler_mongo.data_get()
    d = data[k]
    data_name = d['name']
    data_src = d['src']
    data_intro = d['intro']   
    t.insert(INSERT, data_name)
    t.insert(INSERT, data_intro)
    t.insert(INSERT, data_src)

    img_r = requests.get(d['src'])
    imgData = img_r.content
    imgPath = 'a.jpeg'
    with open(imgPath, 'wb') as f:
        f.write(imgData)
    img = Image.open('a.jpeg')
    Photo =ImageTk.PhotoImage(image=img)
    c.create_image(0, 0, anchor='nw', image=Photo)


def button_next():
    global i
    i = i+1
    button_img(i)

def button_delete():
    crawler_mongo.delete()


window = Tk()
window.title("获取小说图片")
win_s = window.winfo_screenwidth()
win_h = window.winfo_screenheight()
root_s = win_s/2
root_h = win_h/2-100
window.geometry('%dx%d+%d+%d' % (root_s,root_h,400,250))#使界面显示位置近似居中

# scroll = Scrollbar()

t = scrolledtext.ScrolledText(window)
t.grid(row=4, column=0, columnspan=2, padx=1, pady=2)

c = Canvas(window, width=240, height=320, bg='gray')
try:
    img = Image.open('a.jpeg')
    Photo =ImageTk.PhotoImage(image=img)
    c.create_image(0, 0, anchor='nw', image=Photo)
except:
    pass
c.grid(row=4, column=2, columnspan=2, padx=1, pady=2)

i = 0

Button(window, text='开始爬取', command=lambda:button_download()).grid(row=3, column=0, sticky=W, pady=3)
Button(window, text='显示数据', command=lambda:button_show()).grid(row=3, column=1, sticky=W, pady=3)
Button(window, text='显示图片', command=lambda:button_img(i)).grid(row=3, column=2, sticky=W, pady=3)
Button(window, text='下一张图片', command=lambda:button_next()).grid(row=3, column=3, sticky=W, pady=3)
Button(window, text='清除数据',  command=lambda:button_delete()).grid(row=3, column=4, sticky=W, pady=3)

window.mainloop()