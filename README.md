# Lab 3 Addendum - Arp spoofing

### Introduction
Now that you are done with Lab 3 we can cover one of the challenges that was
taken out prior to the lab being assigned, ARP spoofing.

Note: this is NOT a required/graded piece, just done over in class.

### Background
In the original version of scapyhunt, the final FTP server is configured to not
respond to most IP addresses.  In this exercise we re-enable that rule
and require you to use an additional technique to access the server, arp spoofing.

Take a look at [ceg4900 - lab 3](https://github.com/mkijowski/ceg-4900-lab3) for
our previous work.



### Resources
* [The scapy python library](https://scapy.net/)
* [`/scapy-hunt`](../master/scapy-hunt)
* [`/code`](../master/code/)
* Parrot OS
* [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol)
* [ARP spoofing](https://en.wikipedia.org/wiki/ARP_spoofing)
* [Man-in-the-middle attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)

### Task 1 - So what changed
Not a whole lot to begin with.  We launch our simulated network with:
``` 
sudo python ~/ceg-4900-lab3/scapy-hunt/scapyHunt.py
```
We perform our cam overflow with the included `code/cam-overflow.py`

We capture, alter, and send the port knock sequence with `code/knock.py`

And now things get intersting.  Hopefully you all caught the IP of the FTP 
server in question `10.1.8.6`.  In this version of `scapyhunt` this server
only responds to a specific IP.

* What IP in scapyhunt should we be attempting to spoof for our FTP traffic to be
  accepted by `10.1.8.6` (consult `tcpdump`)?

### Task 2 - Spoof
Lets look at a basic arp spoof in scapy.

What are we trying to accomplish?  Well, to be a true Man-in-the-middle we need
our target to think we are the gateway (or other spoofed system), and we need
the gateway (or other spoofed system) to think we are the target.  So lets get
our info together:

* target_ip = "10.1.8.6"
* target_mac = "???"
* gateway_ip = "10.5.0.6"
* gateway_mac = "???"

Where do we get the Mac addresses?  Easy, check the network.

Now lets get poisoning.

We need to send two packets, one to the target, telling it that the IP address
belonging to the spoofed system has **OUR Mac address**.

The second to the spoofed system telling it that the IP address of the Target has **OUR Mac address**.

In scapy:
```
poison_target = ARP()
poison_target.op   = 2
poison_target.psrc = gateway_ip
poison_target.pdst = target_ip
poison_target.hwdst= target_mac
#   poison_targe.hwsrc= local_mac

poison_gateway = ARP()
poison_gateway.op   = 2
poison_gateway.psrc = target_ip
poison_gateway.pdst = gateway_ip
poison_gateway.hwdst= gateway_mac
#   poison_gateway.hwsrc= local_mac
```
Hopefully these packets are pretty obvious.  But we still need a lot of logic
wrapped around it and for that I refer to [code/arper.py](../master/code/arper.py)


### Acknowledgement
Huge shoutout to [jfsulliv](https://github.com/jfsulliv) for uploading scapyhunt!

