import tkinter

top = tkinter.Tk()

quit = tkinter.Button(top, text='hello, world!', command=top.quit
                      )
quit.pack()

tkinter.mainloop()