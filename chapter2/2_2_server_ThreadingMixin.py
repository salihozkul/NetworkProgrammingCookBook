#!/usr/bin/env python

import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0 #tells the kernel to pick up a port dynamically
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'

def client(ip, port, message):
    """ A client to test threading mixin server """
    #Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Connect to the server
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        print "Client received: %s" % response
    finally:
        sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    """ An example of threaded TCP request handler """
    def handle(self):
        #Send the echo back to the client
        data = self.request.recv(BUF_SIZE)
        current_thread = threading.current_thread()
        response = '%s: %s' % (current_thread.name, data)
        print "Server sending response [current_thread: data] = [%s]" % response
        self.request.sendall(response)
        return

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """ Nothing to add here, inherited everything from parents """
    pass

def main():
    #Launch server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address # retrieve ip and port
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print "Server loop running PID %s" % os.getpid()
    
    #Launch clients
    
    client(ip,port, "Client1 : Hello !!! ")
    client(ip,port, "Client2 : Hello !!! ")
    client(ip,port, "Client3 : Hello !!! ")
    
    #clean up
    server.shutdown()
    server.socket.close()
    

if __name__ == '__main__':
    main()
