import sys
from tkinter import *

def theSuprise():
    inString = daString.get()
    inString = inString + " knows about python"
    myHideLabel = Label(theGui,text=inString,fg="purple").pack()


theGui = Tk()
daString = StringVar()

theGui.geometry('450x450+200+200')

theGui.title("My first dumb python TK app")

myLabel = Label(text='Best Label ever',fg='blue',bg='yellow').place(x=100,y=100)
#myGrid = Label(text='EL GRID is bigger',fg='red',bg='green').grid(row=0,column=0)
myButton = Button(theGui,text="OK",command=theSuprise,fg="green",bg="red").place(x=110,y=150)

mEntry = Entry(theGui,textvariable=daString).pack()


theGui.mainloop()
