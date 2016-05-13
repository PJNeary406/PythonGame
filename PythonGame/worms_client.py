'''
Created on May 9, 2016
@author: stephen.neary
'''


from Tkinter import *
from PythonGame import ClientSocket

class Worms():
    def __init__(self):
        self.root = Tk()
        self.sock = ClientSocket.ClientSocket()
        self.title = Label(self.root, text="Python Study Group Worms v0.1",fg="black")
        self.user_name_label = Label(self.root, text="Username:", fg="black")
        self.password_name_label = Label(self.root, text="Password:", fg="black")
        self.user_name_input = Entry(self.root)
        self.password_input = Entry(self.root)
        self.input_button = Button(self.root, text="Login", width=10, command=self.authenticate)

    def init_screen_widgets(self):

        self.root.geometry("500x500")
        self.title.place(x=150, y=0)
        self.user_name_label.place(x=130, y=50)
        self.password_name_label.place(x=130, y=80)
        self.user_name_input.place(x=200, y=52)
        self.password_input.place(x=200, y=82)
        self.input_button.place(x=230, y=100)
        self.sock.connect()
        self.root.mainloop()

    def authenticate(self):

        user_name = self.user_name_input.get()
        password = self.password_input.get()

        self.sock.send_message(""+user_name+","+password)


if __name__ == '__main__':

    screen = Worms()
    screen.init_screen_widgets()



