#!/usr/bin/env python
import socket
import fcntl
import struct
import argparse
import nmap

SAMPLE_PORTS = '21-23'

def get_interface_status(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_addres = socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
    nm = nmap.PortScanner()
    nm.scan(ip_addres, SAMPLE_PORTS)
    return nm[ip_addres].state()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python networking utils')
    parser.add_argument('--ifname', action="store", dest="ifname", required=True)
    given_args = parser.parse_args()
    ifname = given_args.ifname
    print "Interface [%s] is : %s" % (ifname, get_interface_status(ifname))