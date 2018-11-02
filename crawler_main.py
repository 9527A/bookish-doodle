from tkinter import *

window = Tk()
window.title("hello world")
win_s = window.winfo_screenwidth()
win_h = window.winfo_screenheight()
root_s = win_s/2-350
root_h = win_h/2-100
window.geometry('%dx%d+%d+%d' % (root_s,root_h,500,250))

l_1 = Label(window, text='user name')
l_1.grid(row=1, column=0, sticky=N+E+S+W)

var_1 = StringVar()
e_1=Entry(window, textvariable=var_1)
e_1.grid(row=1, column=1, sticky=N+E+S+W)

l_2 = Label(window, text='passworld')
l_2.grid(row=2, column=0, sticky=N+E+S+W)

var_2 = StringVar()
e_2 = Entry(window, textvariable=var_2, show='*')
e_2.grid(row=2, column=1, sticky=N+E+S+W)

Button(window, text='login').grid(row=3, column=0, sticky=N+S)
Button(window, text='sign up').grid(row=3, column=1, sticky=N+S)


window.mainloop()