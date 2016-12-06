#!/usr/bin/python
#-*-coding:utf-8-*-

#author=yanislong

from scapy.all import *
import sys, os

if os.geteuid() != 0:
    print "this program must be run as root"
    sys.exit()
if len(sys.argv) < 2:
    print "please use %s x.x.x" %(sys.argv[0])
    sys.exit()
conf.verb = 0
ipscan = sys.argv[1] + ".0/24"
f = file("/root/scan_result.txt","w")
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ipscan),timeout=2)
print ans[0]
for snd, rcv in ans:
    print rcv
    list_mac = rcv.sprintf("%Ether.src% -> %ARP.psrc%")
    print rcv.sprintf("%Ether.src% -> %ARP.psrc%")
    f.write(list_mac +'\n')
f.close()
