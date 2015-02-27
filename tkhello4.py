# coding: utf-8
# filename: tkhello4.py

from tkinter import *

def resize(en=None):
	label.config(font='Helvetica -%d bold' % scale.get())

top = Tk()
top.geometry('250x150')

label = Label(top, text="Hello World!", font='Helvetica -12 bold')
label.pack()

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)

quit=Button(top, text="QUIT", command=top.quit, activeforeground='white', activebackgroun='red')
quit.pack()

mainloop()


