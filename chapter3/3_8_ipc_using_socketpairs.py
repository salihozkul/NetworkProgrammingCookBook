#!/usr/bin/env python
import socket
import os

BUFFSIZE = 1024

def test_socketpair():
    """ Test Unix socketpair """
    parent, child = socket.socketpair()
    pid = os.fork()
    try:
        if pid:
            print "@Parent, sending message..."
            child.close()
            parent.sendall("Hello from parent!")
            response = parent.recv(BUFFSIZE)
            print "Response from child:", response
            parent.close()
        else:
            print "@Child, waiting for message from parent"
            parent.close()
            message = child.recv(BUFFSIZE)
            print "Message from parent:", message
            child.sendall("Hello from child!")
            child.close()
            
    except Exception, e:
        print "Error: %s" % e 
        
if __name__ == '__main__':
    test_socketpair()