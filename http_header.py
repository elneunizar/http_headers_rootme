#!/usr/bin/env python
import urllib2
import re
import sys, getopt
#Get method to get the page
host=""
def request(host):
    req=urllib2.Request(host)
    return req

def getpage(host):
    req=request(host)
    res=urllib2.urlopen(req)
    the_page=res.read()
    #read the header information
    header=res.info()
    print 'Header:\n%s\nData:\n%s' %(header,the_page)
    return header

def mod_header(e,v):
    global host
    req=request(host)
    req.add_header(e,v)
    res=urllib2.urlopen(req)
    header=res.info()
    the_page=res.read()
    print 'Header:\n%s\nData:\n%s' %(header,the_page)
    return header

def main(argv):
    global host
    try:
        opts,args=getopt.getopt(argv,"ht:ga:",["help=","target=","get=","add="])
    except getopt.GetoptError:
        print 'http_header.py -t -a|-g [argument=value]|[host-address]|[get'
        sys.exit()
    for opt, arg in opts:
        if opt in ("-h","--help"):
            print 'http_header.py -t -a|-g [argument=value]|[host-address]'
        elif opt in ("-t","--target"):
            host=str(arg)
        elif opt in ("-g","--get"):
            if(host!=""):
                getpage(host)
            else:
                print 'http_header.py -t -a|-g [argument=value]|[host-address]'
        elif opt in ("-a","--add"):
            if(re.search("=",arg).group()!="" and host!=""):
                all_arg=arg.split('=')
                mod_header(all_arg[0],all_arg[1])
            else:
                print 'http_header.py -t -a|-g [argument=value]|[host-address]'
                sys.exit()
if __name__ == "__main__":
    main(sys.argv[1:])
