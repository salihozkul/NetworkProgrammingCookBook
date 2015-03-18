#!/usr/bin/env python
import socket
from time import time as now
import argparse

DEFAULT_TIMEOUT = 120
DEFAULT_SERVER_HOST = 'localhost'
DEFAULT_SERVER_PORT = 80

class NetServiceChecker(object):
    """ Wait for a network service to come online """
    def __init__(self, host, port, timeout=DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.scok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def end_wait(self):
        self.scok.close()
        
    def check(self):
        """ Check the service """
        if self.timeout:
            end_time = now() + self.timeout
            
        while True:
            try:
                if self.timeout:
                    next_timeout = end_time - now()
                    if next_timeout < 0:
                        return False
                    else:
                        print "setting socket next timeout %s s" % round(next_timeout)
                        self.scok.settimeout(next_timeout)
                    self.scok.connect((self.host, self.port))
                
            #handle exceptions
            except socket.timeout, err:
                if self.timeout:
                    return False
            except socket.error, err:
                print "Exception: %s" % err
            else: #if all goes well
                self.end_wait()
                return True
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wait for Network Service')
    parser.add_argument('--host', action="store", dest="host", default=DEFAULT_SERVER_HOST)
    parser.add_argument('--port', action="store", dest="port", type=int, default=DEFAULT_SERVER_PORT)
    parser.add_argument('--timeout', action="store", dest="timeout", type=int, default=DEFAULT_TIMEOUT)
    given_args = parser.parse_args()
    host, port, timeout = given_args.host, given_args.port, given_args.timeout
    service_checker = NetServiceChecker(host, port, timeout=timeout)
    print "Checking for network service %s: %s ..." % (host, port)
    if service_checker.check():
        print "Service is available again!"
        
                     