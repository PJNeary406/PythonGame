from tkinter import *


class simpleButton:
    def __init__(self, master, phLabel):
        frame = Frame(master)
        self.newM = phLabel
        frame.pack(side=TOP)
        self.phLabel = phLabel
        self.mButton = Button(frame, text="CLICK ME!", command=self.SwapPic, fg="green", bg="black").pack(side=TOP)

    def SwapPic(self):
        newPhoto = PhotoImage(file="Rage-Face.gif")
        self.newM.configure(self.master,)



root = Tk()
mPhoto = PhotoImage(file="unnamed.png")
photoLabel = Label(root, image=mPhoto)

photoLabel.pack(side=BOTTOM)
junk = simpleButton(root,photoLabel)
root.mainloop()