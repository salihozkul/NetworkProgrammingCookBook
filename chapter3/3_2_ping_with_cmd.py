#!/usr/bin/env python

import shlex
import subprocess

cmd = "ping -c 1 www.google.com"
args = shlex.split(cmd)
try:
    subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print "Google web server is up !"
except subprocess.CalledProcessError:
    print "Failed to get ping"

