#!/usr/bin/python
#-*-coding:utf-*-

#author=yanislong

from scapy.all import *

ip = sr(IP(des="172.16.9.238")/TCP(dport=80))

