'''
Created on May 9, 2016
@author: stephen.neary


yeah a change
All code should adhere to the coding standards define in PEP - 8.
see https://www.python.org/dev/peps/pep-0008/
'''

# imports
import ClientSocket
from Tkinter import *
from threading import Thread
import time

class WormsClient():
    '''
    This class controls all functionality of the Worms clint program.
    Currently it contains code for initializing screen widgets,
    connecting to the worms server, and animating the background gif image.
    This parts may need to be pulled out into there own classes in the future.
    '''

    def __init__(self):

        '''
        This function the class, frame widgets, and public data members
        '''

        # init frame widgets
        self.root = Tk()
        self.title = Label(self.root, text="Python Study Group Worms v0.1",fg="black")
        self.user_name_label = Label(self.root, text="Username:", fg="black")
        self.password_name_label = Label(self.root, text="Password:", fg="black")
        self.user_name_input = Entry(self.root)
        self.password_input = Entry(self.root)
        self.input_button = Button(self.root, text="Login", width=10, command=self.authenticate)
        self.background = Label(self.root, bd=0)

        # init object data members
        self.gif_path = "C:\Users\stephen.neary\Pictures\giphy.gif"
        self.frame_num = 0
        self.sock = ClientSocket.ClientSocket()

    def init_screen_widgets(self):

        ''' This function places screen widgets and sets the size of the screen '''

        # set screen size
        self.root.geometry("500x500")

        # set the background to the back of the frame
        self.background.lower(belowThis=None)

        # place screen widgets
        self.background.place(x=0, y=0)
        self.title.place(x=150, y=0)
        self.user_name_label.place(x=130, y=50)
        self.password_name_label.place(x=130, y=80)
        self.user_name_input.place(x=200, y=52)
        self.password_input.place(x=200, y=82)
        self.input_button.place(x=230, y=100)

    def start(self):

        '''
        This function starts the amination of the background label,
        connects to the worms server, and starts the TK module
        '''

        # start background label animation
        Thread(target=self.animate).start()

        # connect to the worms server
        self.sock.connect()

        # start the TK module
        self.root.mainloop()

    def authenticate(self):

        ''' This function authenticates users login credentials '''

        # get user input
        user_name = self.user_name_input.get()
        password = self.password_input.get()

        # send user input to the server
        self.sock.send_message(""+user_name+","+password)

    def animate(self):

        ''' This function animates the background label '''

        while True:
            try:
                # sleep for 4 milliseconds before drawing each frame
                time.sleep(0.04)

                # create new image
                img = PhotoImage(file=self.gif_path, format="gif - {}".format(self.frame_num))

                # set label image to the new image
                self.background.config(image=img)
                self.background.image = img

                # increment frame count by 1
                self.frame_num += 1
            except:
                self.frame_num = 0

if __name__ == '__main__':

    # init WormsClient object
    screen = WormsClient()

    # init screen widgets
    screen.init_screen_widgets()

    # start the application
    screen.start()



