#!/usr/bin/env python
#importing function named ConnectHandler from module named netmiko
from netmiko import ConnectHandler
from getpass import getpass

Username = input("Enter your ssh username: ")
Password = getpass()
#defining routers parameters in definition.

device_types = ['cisco_ios','cisco_xr']
for devices in device_types:
     if devices == 'cisco_ios':
         for IP_addrs in open('cisco_ios_routers_ip.txt','r').read().splitlines():
            router = {'device_type':devices,'ip':IP_addrs,'username':Username,'password':Password}
            router_ssh = ConnectHandler(**router)
            print('show commands on '+router['ip'])
            print('='*80)
            for show_commands in open('show_commands_ios.txt','r').read().splitlines():
                output = router_ssh.send_command(show_commands)
                print(output)
            print('='*80)
     if devices == 'cisco_xr':
         for IP_addrs in open('cisco_xr_routers_ip.txt','r').read().splitlines():
            router = {'device_type':devices,'ip':IP_addrs,'username':Username,'password':Password}
            router_ssh = ConnectHandler(**router)
            print('show commands on '+router['ip'])
            print('='*80)
            for show_commands in open('show_commands_xr.txt','r').read().splitlines():
                output = router_ssh.send_command(show_commands)
                print(output)
            print('='*80)
