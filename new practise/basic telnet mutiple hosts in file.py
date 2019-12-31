import getpass
import telnetlib
#Open file of management ip addresses of devices
file = open('ip_hosts.txt')
#Ask for user credentials
user = input("Enter your username: ")
password = getpass.getpass()

for HOST in file:
# Below strip() command erases enter space'\n' in the value of variable HOST.
# When strip() command is skipped, the length of the IP address is 10 and when strip()command is added length becomes 9.
    HOST = HOST.strip()
#Below two print statements prints the host ip addresses and length of IP addresses.
#    print(HOST)
#    print("Length =",len(HOST))
    tn = telnetlib.Telnet(HOST)
#Login credentials.
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
#Commands executed.
    tn.write(b"sh ip int br\n")
    tn.write(b"exit\n")
#print the output for each node.
    print(tn.read_all().decode('ascii'))
