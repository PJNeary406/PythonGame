'''
Created on Mar 17, 2016

@author: stephen.neary
'''
import socket
import SocketServer
from threading import Thread

class ClientSocket():

    def __init__(self):
        self.SERVER_LOCATION = ("localhost", 6969)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_response = ""


    def connect(self):
        self.sock.connect(self.SERVER_LOCATION)
        print "Connecting to server %s port %s" % self.SERVER_LOCATION

    def send_message(self, data):
        try:
            self.sock.sendall(data)

            self.server_response = self.sock.recv(1024)

            if self.server_response:
                print "Server response was :", self.server_response

        finally:
            self.sock.close()

    def get_response(self):

        return self.server_response
