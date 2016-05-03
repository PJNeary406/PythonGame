'''
Created on Mar 16, 2016

@author: stephen.neary
'''
import SocketServer
import socket 
from threading import Thread


LOCAL_HOST = ("localhost" , 6969)
    
class service(SocketServer.BaseRequestHandler): 
    def handle(self):
        data = 'dummy'
        print "Client connected with ", self.client_address
        while len(data):
            data = self.request.recv(1024)
            self.request.send(data)

        print "Client exited"
        self.request.close()
        
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    t = ThreadedTCPServer(LOCAL_HOST, service)
    print "init server"
    t.serve_forever()
    
    