#!/usr/bin/env python
#importing function named ConnectHandler from module named netmiko
from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException

Username = input("Enter your ssh username: ")
Password = getpass()

device_types = ['cisco_ios','cisco_xr']
for devices in device_types:    #check device type.
     if devices == 'cisco_ios':
         for IP_addrs in open('cisco_ios_routers_ip.txt','r').read().splitlines():  #open cisco_ios_routers_ip file for device-type cisco_ios.
            router = {'device_type':devices,'ip':IP_addrs,'username':Username,'password':Password}  #defining routers parameters in definition.
            try:        #try below operation. If returned expected error, run operations in that expect function and continue with rest of the string.
                router_ssh = ConnectHandler(**router)
            except (NetMikoAuthenticationException):    #invalid credentials
                print("Authentication error on "+router['ip'])
                continue
            except (NetMikoTimeoutException):   #no mgmt reachability
                print("Timeout error on "+router['ip'])
                continue
            except (SSHException):  #device not responding to ssh request
                print("SSH error: "+router['ip'])
                continue
            #if no error occurred then run rest of the code in loop.
            #if error occurred end 'for IP_addrs loop' and start for other value in for IP_addrs loop.
            print('show commands on '+router['ip'])
            print('='*80)
            for show_commands in open('show_commands_ios.txt','r').read().splitlines(): #read and store each line in sequence (using splitlines()) in object show_commands.
                output = router_ssh.send_command(show_commands) #send each command in loop to the device.
                print(output)
            print('='*80)
     if devices == 'cisco_xr':
         for IP_addrs in open('cisco_xr_routers_ip.txt','r').read().splitlines():
            router = {'device_type':devices,'ip':IP_addrs,'username':Username,'password':Password}
            try:
                router_ssh = ConnectHandler(**router)
            except (NetMikoAuthenticationException):
                print("Authentication error on "+router['ip'])
                continue
            except (NetMikoTimeoutException):
                print("Timeout error on "+router['ip'])
                continue
            except (SSHException):
                print("SSH error: "+router['ip'])
                continue
            print('show commands on '+router['ip'])
            print('='*80)
            for show_commands in open('show_commands_xr.txt','r').read().splitlines():
                output = router_ssh.send_command(show_commands)
                print(output)
            print('='*80)
