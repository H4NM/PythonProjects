#!/usr/bin/python

from socket import * 
import optparse
from threading import *
import time

def connScan(tgtHost, tgtPort, tgtShowPorts):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print('[+] %d/tcp Open' %tgtPort)
    except:
        if tgtShowPorts == True:
            print('[-] %d/tcp Closed' %tgtPort)
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts, tgtShowPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Unable to resolve %s address' % tgtHost)
    try:
        tgtName = gethostbyaddress(tgtIP)
        print('[+] Scan results for: ' + tgName[0])
    except:
        print('[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort), tgtShowPorts))

        #There was a threading runtime error where too many threads were created
        #This while loop enables for the rest of the threads to finish and complete before overloading
        #active_count variable comes from threading module
        if active_count()>200 :
            time.sleep(2)
        t.start()
        

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports> -c <show closed ports>')
    parser.add_option('-H',
                      dest='tgtHost',
                      type='string',
                      help='specify target host')
    parser.add_option('-p',
                      dest='tgtPort',
                      type='string',
                      help='specify target ports separated by comma OR enter "rp"'
                      ' for registered ports OR "dp" for dynamic ports')

    parser.add_option("-c",
                      "--closed",
                      action="store_true",
                      dest="showClosed",
                      default=False,
                      help="Print out the closed ports")

    options, args = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    tgtShowPorts = options.showClosed

    if tgtHost == None:
        print(parser.usage)
        exit(0)
    if tgtPorts[0] == 'None':
        wellknown_port_list = list(range(1, 1023))
        tgtPorts = wellknown_port_list
    elif tgtPorts[0] == 'rp':
        registered_ports = list(range(1024, 49151, 1))
        tgtPorts = registered_ports
    elif tgtPorts[0] == 'dp':
        dynamic_ports = list(range(49152, 65535, 1))
        tgtPorts = dynamic_ports
    else:
        print(parser.usage)
        exit(0)

    portScan(tgtHost, tgtPorts, tgtShowPorts)

if __name__ == '__main__':
    main()
