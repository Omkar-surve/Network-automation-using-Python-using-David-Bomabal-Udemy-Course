import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

file = open('ip_hosts.txt')
for HOST in file:
# Below strip() command erases enter space'\n' in the value of variable HOST.
# When strip() command is skipped, the length of the IP address is 10 and when strip()command is added length becomes 9.
    HOST = HOST.strip()
#Below two print statements prints the host ip addresses and length of IP addresses.
    print(HOST)
    print("Length =",len(HOST))
    tn = telnetlib.Telnet(HOST)
#Login credentials.
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
#Commands executed.
    tn.write(b"terminal length 0\n")
    tn.write(b"sh running-config\n")
    tn.write(b"exit\n")
#print the output for each node.
    readfile = tn.read_all().decode('ascii')
    writefile = open("Backup for "+HOST+".txt","w")
    writefile.write(readfile)
    writefile.write("\n")
    writefile.close()
