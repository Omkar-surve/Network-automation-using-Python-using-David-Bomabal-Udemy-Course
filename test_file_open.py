import getpass
import telnetlib

file = open('switches_mgmt_ip')
for IP in file:
    IP = IP.strip()
    print("Configuring switch: "+(IP)+b"\n")
