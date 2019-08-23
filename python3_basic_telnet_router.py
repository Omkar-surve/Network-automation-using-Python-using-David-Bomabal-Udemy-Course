import getpass
import telnetlib

HOST = "10.10.0.4"
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
tn.write(b"int loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"description Interface made using python script\n")
tn.write(b"router ospf 10\n")
tn.write(b"router-id 1.1.1.1\n")
tn.write(b"network 1.1.1.1 0.0.0.0 area 0\n")
tn.write(b"do wr me\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
