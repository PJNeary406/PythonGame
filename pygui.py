from tkinter import *
from tkinter import messagebox

def theSuprise():
    inString = daString.get()
    if inString == "":
        inString = "No one"
    inString += " smells bad"
    myHideLabel = Label(theGui, text=inString, fg="purple").pack()
    return

def mClose():
    theGui.quit()
    return

def mAbout():
    messagebox.showinfo(title="About this horrible gui app",
                       message="This is probably the worst app ever made in 30 min.")

    return

theGui = Tk()
daString = StringVar()
theGui.geometry('450x450+200+200')

theGui.title("My first dumb python TK app")

myLabel = Label(text='Le Label', fg='blue', bg='yellow').pack()
# myGrid = Label(text='EL GRID is bigger',fg='red',bg='green').grid(row=0,column=0)
myButton = Button(theGui, text="Compute!", command=theSuprise, fg="green", bg="red").pack()
mEntry = Entry(theGui, textvariable=daString).pack()

menubar = Menu(theGui)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Close", command=mClose)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=mAbout)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Help", menu=helpmenu)
theGui.config(menu=menubar)

spinbox1 = Spinbox(theGui, from_=0, to_=10).pack(side=BOTTOM)
theGui.mainloop()
