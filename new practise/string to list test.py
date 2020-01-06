import getpass
import telnetlib

#user = input("Enter your username: ")
#password = getpass.getpass()

##Converts strings to list:

file = open('ip_hosts.txt')
for HOST in file:
    abc = HOST.split()
print (abc)


##Converts lists to strings:

file = open('ip_hosts.txt')
for HOST in file:
    abc = HOST.join(" ")
print (*abc)
