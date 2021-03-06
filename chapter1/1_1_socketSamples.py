#!/usr/bin/env python

import socket

def print_local_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host name : %s" % host_name
    print "IP address: %s" % ip_address
    
def print_remote_machine_info():
    remote_host = 'www.python.org'
    try:
        print "IP address: %s" % socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s: %s" % ( remote_host, err_msg)
    
if __name__ == '__main__':
    print_local_machine_info() 
    print_remote_machine_info()