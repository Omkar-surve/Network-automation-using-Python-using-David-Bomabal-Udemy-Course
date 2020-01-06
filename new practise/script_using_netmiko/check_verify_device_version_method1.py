#!/usr/bin/env python
#importing function named ConnectHandler from module named netmiko
from netmiko import ConnectHandler
from getpass import getpass

Username = input("Enter your ssh username: ")
Password = getpass()

read_version = 0    #Counter to indicate starting point of the match in the string.
SW_version_list = ['I86BI_LINUX-ADVENTERPRISEK9-M','Cisco IOS XR Software, Version 6.0.0']
#defining routers parameters in definition.
for SW_version in SW_version_list:
    device_types = ['cisco_ios','cisco_xr']
    for devices in device_types:
         if devices == 'cisco_ios':
             if SW_version == 'I86BI_LINUX-ADVENTERPRISEK9-M':
                 for IP_addrs in open('cisco_ios_routers_ip.txt','r').read().splitlines():
                    router = {'device_type':devices,'ip':IP_addrs,'username':Username,'password':Password}
                    router_ssh = ConnectHandler(**router)
                    print('show commands on '+router['ip'])
                    print('='*80)
                    output = router_ssh.send_command('show version')
                    read_version = output.find(SW_version)
                    if read_version>0:
                        print('Version: '+SW_version)
                        for show_commands in open('show_commands_ios.txt','r').read().splitlines():
                            output = router_ssh.send_command(show_commands)
                            print(output)
                            print('='*80)
         if devices == 'cisco_xr':
             if SW_version == 'Cisco IOS XR Software, Version 6.0.0':
                 for IP_addrs in open('cisco_xr_routers_ip.txt','r').read().splitlines():
                    router = {'device_type':devices,'ip':IP_addrs,'username':Username,'password':Password}
                    router_ssh = ConnectHandler(**router)
                    print('show commands on '+router['ip'])
                    print('='*80)
                    output = router_ssh.send_command('show version')
                    read_version = output.find(SW_version)
                    if read_version>0:
                        print('Version: '+SW_version)
                        for show_commands in open('show_commands_xr.txt','r').read().splitlines():
                            output = router_ssh.send_command(show_commands)
                            print(output)
                            print('='*80)
