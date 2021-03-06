#!/usr/bin/env python
"""Encrypting and Decrypting contents of the file using JSON"""
from netmiko import ConnectHandler
from simplecrypt import encrypt, decrypt
import json
import csv
from getpass import getpass
from pprint import pprint
from time import time
import threading
from multiprocessing import Pool

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""Generating dictionaries of device creds"""

def devices_detail(devices_info, creds_list):
    devices = {}
    for device_line in devices_info:
        for cred_line in creds_list:
            if device_line[1] == cred_line[0]:
                device = {'device_type':device_line[0],'ip':cred_line[0],'username':cred_line[1],'password':cred_line[2]}
        devices[device['ip']] = device
    return devices

"""Backup config of devices"""

def write_config(device_type,device_ip,router_ssh):
    print(">>>>>>>>>>Copying config of router "+device_ip)
    if device_type == 'cisco_ios':
        with open('Cisco_IOS_config_backup_for_'+device_ip,'w') as f:
            output = router_ssh.send_command('show run')
            f.write(output)
    if device_type == 'cisco_xr':
        with open('Cisco_XR_config_backup_for_'+device_ip,'w') as f:
            output = router_ssh.send_command('show run')
            f.write(output)
    return

"""SSH and configure devices"""

def configuring_device(dev_list):
    dev = tuple(dev_list)
    device = {'device_type':dev[0],'ip':dev[1],'username':dev[2],'password':dev[3]}
    router_ssh = ConnectHandler(**device)
    if device['device_type'] == 'cisco_ios':
        print('SSH to cisco ios device '+device['ip'])
        write_config(device['device_type'],device['ip'],router_ssh)
    if device['device_type'] ==  'cisco_xr':
        print('SSH to cisco XR device '+device['ip'])
        write_config(device['device_type'],device['ip'],router_ssh)
    return

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                       MAIN SCRIPT
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

creds_data = input("Enter name of encrypted credentials file (default: encrypted_cred):") or "encrypted_cred"
devices_data = input("Enter name of the devices info file (default: devices_info.csv):") or "devices_info.csv"
password = getpass()
no_of_threads = Pool(int(input("Enter no. of threads(default 3):") or "3"))

start_time = time()
#below json.loads() command converts encrypted_cred_read.read() bytes data to list which is then decrypted using password as salt
devices_raw_data = csv.reader(open(devices_data,'r'))
devices_list = [devices_info for devices_info in devices_raw_data]
pprint(devices_list)
#below json.loads() command converts encrypted_cred_read.read() bytes data to list which is then decrypted using password as salt
creds_list = json.loads(decrypt(password,open(creds_data,'rb').read()))

new_device_list = []
devices_info = devices_detail(devices_list,creds_list)
for [k,v] in devices_info.items():
    new_device_list.append((v['device_type'],v['ip'],v['username'],v['password']))
no_of_threads.map(configuring_device,new_device_list)
#no_of_threads.close()
#no_of_threads.join()

#no_of_threads.map(configuring_device, args = (v['device_type'],v['ip'],v['username'],v['password']))

print('Elapsed time:'+str(time()-start_time)+'sec')
