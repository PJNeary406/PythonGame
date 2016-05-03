'''
Created on Mar 17, 2016

@author: stephen.neary
'''
import socket 
import SocketServer
from threading import Thread

SERVER_LOCATION = ("localhost" , 6969)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
message = ""

if __name__ == '__main__':
    sock.connect(SERVER_LOCATION)
    print "Connecting to server %s port %s" % SERVER_LOCATION
    
    try:
        while message != "END":
            message = raw_input("Enter message:")
            sock.sendall(message)
            
            data = sock.recv(1024)
            
            if data:
                print "Server responce was :",data
            
            if data == "END":
                break;
            
    finally:
        sock.close()  
       
