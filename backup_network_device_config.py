import getpass
import telnetlib

username = input("Enter your telnet username: "+"\n")
password = getpass.getpass()

print("User "+username+" logged in")
#print()

file = open('switches_mgmt_ip')

for IP in file:
    print("Backup running config for switch "+IP+"\n")
    IP = IP.strip()
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(username.encode('ascii')+b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii')+b"\n")
    tn.write(b"enable \n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii')+b"\n")
    tn.write(b"terminal length 0 \n")
    tn.write(b"sh run \n")
    tn.write(b"exit \n")
    print(tn.read_all().decode('ascii')+"\n")
