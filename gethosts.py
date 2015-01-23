#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re

def write_hosts(f):
    url = "http://www.360kb.com/kb/2_122.html"
    response = urllib2.urlopen(url)
    start = False
    while True:
        line = response.readline()
        if start == False and "#google hosts 2015 by 360kb.com" in line:
            start = True
        if start == True:
            line = line.replace("&nbsp;", "")
            line = re.sub("<[^>]+>", "", line)
            f.write(line)
            #print line 
        if start == True and "#google hosts 2015 end" in line:
            start = False
            break
    
def main():
    #f_name = "C:\Windows\System32\drivers\etc\hosts"
    f_name = "hosts"
    f = open(f_name,"w")
    write_hosts(f)
    f.close()


if __name__ == "__main__":
    main()

