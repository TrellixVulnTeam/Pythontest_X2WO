from tkinter import *
def new_file():
	print("Open new file")

def stub_action():
	print("Menu select")

def open_file():
	print("Opent existing file")



def makeCommandMenu():
	CmdBtn = Menubutton(mBar, text='Button Commands', underline=0)
	CmdBtn.pack(side=LEFT, padx="2m")
	CmdBtn.menu = Menu(CmdBtn)

	CmdBtn.menu.add_command(label="Undo")
	CmdBtn.menu.entryconfig(0, state=DISABLED)

	CmdBtn.menu.add_command(label='New...', underline=0,command=new_file)
	CmdBtn.menu.add_command(label='Open...', underline=0,command=open_file)
	CmdBtn.menu.add_command(label='Wild Font', underline=0, font='Arial', command=stub_action)
	#sCmdBtn.menu.add('seperator')
	CmdBtn.menu.add_command(label='Quit', underline=0, background='white', activebackground='green', command=CmdBtn.quit)

	CmdBtn['menu'] = CmdBtn.menu
	return CmdBtn

def makeCascadeMenu():
	CasBtn = Menubutton(mBar, text='Cascading Menus', underline=0)
	CasBtn.pack(side=LEFT, padx="2m")
	CasBtn.menu = Menu(CasBtn)
	CasBtn.menu.choices = Menu(CasBtn.menu)
	CasBtn.menu.choices.wierdones = Menu(CasBtn.menu.choices)

	CasBtn.menu.choices.wierdones.add_command(label='A')
	CasBtn.menu.choices.wierdones.add_command(label='B')
	CasBtn.menu.choices.wierdones.add_command(label='C')
	CasBtn.menu.choices.wierdones.add_command(label='D')

	CasBtn.menu.choices.add_command(label='A')
	CasBtn.menu.choices.add_command(label='B')
	CasBtn.menu.choices.add_command(label='C')
	CasBtn.menu.choices.add_command(label='D')
	CasBtn.menu.choices.add_command(label='E')
	CasBtn.menu.choices.add_command(label='F')
	CasBtn.menu.choices.add_command(label='G')

	CasBtn.menu.add_cascade(label='Script')
	CasBtn['menu']=CasBtn.menu
	return CasBtn


root = Tk()
mBar = Frame(root, relief=RAISED, borderwidth=2)


CmdBtn = makeCommandMenu()
CasBtn = makeCascadeMenu()

mBar.tk_menuBar(CmdBtn,CasBtn)


mBar.pack(fill=X)
root.title('Menus')
root.mainloop()

