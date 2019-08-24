import getpass
import telnetlib
import os

username = input("Enter your telnet username: "+"\n")
password = getpass.getpass()

print("User "+username+" logged in")
#print()

file = open('switches_mgmt_ip')

for IP in file:
    print("Backup running config for switch "+IP+"\n")
    IP = IP.strip()
#    HOST = IP
    tn = telnetlib.Telnet(IP)
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

    running_config = tn.read_all()
    save_running_config = open('Switch '+IP,'w')
    save_running_config.write(running_config.decode('ascii'))
    save_running_config.close()

    print("Running config for switch "+IP+" is saved in file "+"Switch "+IP+"\n")
#    print(tn.read_all().decode('ascii')+"\n")
