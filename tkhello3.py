import tkinter

top = tkinter.Tk()
hello = tkinter.Label(top, text="Hello World!")
hello.pack()

quit =tkinter.Button(top, text='quit',command=top.quit,bg='red', fg='white')
quit.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()
