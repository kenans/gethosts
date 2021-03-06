#!/usr/bin/python
# -*- coding: utf-8 -*-

# Filename: gethosts.py
# This script is to fetch an available hosts file for goolge in China
# Author: kenansun0@gmail.com
# Date: 01/2015

import urllib2
import re
import os
import socket

def write_hosts(f):
    '''Try to get hosts file content from the Internet.
returns -1 if url is no longer valid
        -2 if no hosts found
         0 otherwise'''
    try:
        url = "http://www.360kb.com/kb/2_122.html"
        #url = "http://www.360kb.com/kb/2_150.html"
    except:
        return -1
    response = urllib2.urlopen(url)
    start = False
    while True:
        line = response.readline()
        if line == '':
            return -2
        if start == False and "#google" in line and "hosts" in line:
            start = True
            f.write("#google hosts begin\n")
            continue
        if start == True:
            line = line.replace("&nbsp;", "")
            line = re.sub("<[^>]+>", "", line)
            f.write(line)
            #print line 
        if start == True and "#google" in line and "hosts" in line:
            start = False
            return 0
def main():
    f_name = "hosts"
    lines = []
    try:
        print "Reading reserved.txt..."
        f = open('reserved.txt')
        lines = f.readlines()
        print "Read reserved.txt successfully"
    except:
        print "reserved.txt not found"
        pass
    import os
    has_old_file = False
    if f_name in os.listdir('.'):
        os.rename(f_name, f_name + '_bk') 
        has_old_file = True
    try:
        with open(f_name, 'w') as f:
            f.write('127.0.0.1\t%s%s' % (socket.gethostname(), os.linesep))
            for line in lines:
                f.write(line)
            ret = write_hosts(f)
            return ret
    except:
        print 'Error: unable to create', f_name, 'file'

if __name__ == "__main__":
    res = main()
    if res != 0:
        # We got an error here
        # Should it send back an email to us ??
        # We only handle the error by printing some info to the console
        # TODO
        if res == -1:
            print "Invalid url!"
        elif res == -2:
            print "Hosts not found!"
    else:
        print "All done"
