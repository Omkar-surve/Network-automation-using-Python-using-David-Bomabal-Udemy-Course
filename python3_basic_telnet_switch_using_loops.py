import getpass
import telnetlib

HOST = "10.10.0.5"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"conf t\n")

for n in range(2,11):
    tn.write(b"vlan "+str(n).encode('ascii')+b"\n")
    tn.write(b"name VLan_"+str(n).encode('ascii')+b"_Python\n")
    tn.write(b"int vlan "+str(n).encode('ascii')+b"\n")
    tn.write(b"description mgmt/gateway for vlan "+str(n).encode('ascii')+b"\n")
    tn.write(b"ip address 192.168."+str(n).encode('ascii')+b"."+str(n).encode('ascii')+b" 255.255.255.0\n")
    tn.write(b"no shutdown\n")
tn.write(b"do wr me\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
