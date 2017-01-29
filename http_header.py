#!/usr/bin/env python
import urllib2
import re
import sys, getopt
#Get method to get the page
URL="http://challenge01.root-me.org/web-serveur/ch5/"
def request():
    req=urllib2.Request(URL)
    return req

def getpage():
    req=request()
    res=urllib2.urlopen(req)
    the_page=res.read()
    #read the header information
    header=res.info()
    print 'Header:\n%s\nData:\n%s' %(header,the_page)
    return header

def mod_header(e,v):
    req=request()
    req.add_header(e,v)
    res=urllib2.urlopen(req)
    header=res.info()
    the_page=res.read()
    print 'Header:\n%s\nData:\n%s' %(header,the_page)
    return header

def main(argv):
    try:
        opts,args=getopt.getopt(argv,"he:v:",["help=","element=","value="])
        getpage()
    except getopt.GetoptError:
        print 'http_header.py -e [argument] [value]'
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h","--help"):
            print 'http_header.py -e [argument] [value]'
        elif opt in ("-e","--element"):
            e=arg
        elif opt in ("-v","--value"):
            v=arg
    if (e !='' and v!=''):
            mod_header(e,v)
if __name__ == "__main__":
    main(sys.argv[1:])
