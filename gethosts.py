#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re

def write_hosts(f):
    '''Try to get hosts file content from the Internet.
returns -1 if url is no longer valid
        -2 if no hosts found
         0 otherwise'''
    try:
        url = "http://www.360kb.com/kb/2_122.html"
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
    f = open(f_name,"w")
    res =  write_hosts(f)
    f.close()
    return res
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
