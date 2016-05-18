'''
Created on May 11, 2016

@author: stephen.neary
'''

from threading import Thread
from Tkinter import *
import time
import os


class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH)
        self.gif_path = "C:\Users\PJ\Pictures\\new_gif.gif"
        root.protocol("WM_DELETE_WINDOW", self.close)

        root.geometry("300x300")

        self.num = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, bd=0)
        self.label.pack()

        Thread(target=self.animate).start()

    def animate(self):
        while True:
            try:
                time.sleep(0.05)
                img = PhotoImage(file=self.gif_path, format="gif - {}".format(self.num))

                self.label.config(image=img)
                self.label.image = img

                self.num += 1
            except:
                self.num = 0

    def close(self):
        os._exit(0)


root = Tk()

app = Application(root)


root.mainloop()
