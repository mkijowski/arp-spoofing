### Solutions guide

### Task 1

`sudo python ~/ceg-4900-lab-3/scapy-hunt/scapyHunt.py` should start the hunt.

1. 10.5.0.0/24
2. `sudo nmap -e tap0 10.5.0.0/24` gives us the following:
   ```
   Nmap scan report for 10.5.0.4
   Host is up (0.045s latency).
   Not shown: 995 closed ports
   PORT    STATE SERVICE
   20/tcp  open  ftp-data
   21/tcp  open  ftp
   22/tcp  open  ssh
   80/tcp  open  http
   443/tcp open  https
   MAC Address: 12:67:7E:B7:6D:04 (Unknown)

   Nmap scan report for 10.5.0.6
   Host is up (0.022s latency).
   Not shown: 997 closed ports
   PORT   STATE    SERVICE
   22/tcp open     ssh
   25/tcp filtered smtp
   80/tcp open     http
   MAC Address: 12:67:7E:B7:6D:06 (Unknown)

   Nmap scan report for 10.5.0.35
   Host is up (0.044s latency).
   Not shown: 993 closed ports
   PORT     STATE SERVICE
   20/tcp   open  ftp-data
   21/tcp   open  ftp
   22/tcp   open  ssh
   25/tcp   open  smtp
   80/tcp   open  http
   443/tcp  open  https
   8080/tcp open  http-proxy
   MAC Address: 12:67:7E:B7:6D:23 (Unknown)
   ```
3. `sudo tcpdump -i tap0` gives us no traffic on the interface.


### Task 2
1. Hub vs switch, primary difference is switches keep track of Mac addresses (in
   the CAM table) and only send traffic to the port that mac address is plugged
   in to.
2. See above
3. Overflow the CAM table so the switch doesn't know where to send traffic, this
   results in the switch defaulting to "hub mode" meaning all packets are sent
   to all devices.
4. See `cam-overflow.py`
5. Re run `sudo tcpdump -i tap0`

### Task 3
1. New traffic between .4 and .6.  More interesting, it appears .6 is listening
   on port 20 (ftp).
2. describe port knocking (hint, .6 is requiring a port knowck before opening
   port 20). https://en.wikipedia.org/wiki/Port_knocking
   ```
15:52:08.691912 IP 10.5.0.4.51753 > 10.5.0.6.951: Flags [S], seq 0, win 2048, length 0
15:52:08.692971 IP 10.5.0.4.51754 > 10.5.0.6.951: Flags [S], seq 0, win 2048, length 0
15:52:08.694058 IP 10.5.0.4.51755 > 10.5.0.6.4826: Flags [S], seq 0, win 2048, length 0
15:52:08.695039 IP 10.5.0.4.51756 > 10.5.0.6.https: Flags [S], seq 0, win 2048, length 0
15:52:08.695996 IP 10.5.0.4.51757 > 10.5.0.6.100: Flags [S], seq 0, win 2048, length 0
15:52:08.696954 IP 10.5.0.4.51758 > 10.5.0.6.ftp: Flags [S], seq 0, win 2048, length 0
   ```


