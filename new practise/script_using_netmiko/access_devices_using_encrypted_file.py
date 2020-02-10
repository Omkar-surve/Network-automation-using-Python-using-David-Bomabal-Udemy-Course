#!/usr/bin/env python
"""Importing libraries and its functions"""
from netmiko import ConnectHandler
from simplecrypt import encrypt, decrypt
import json
import csv
from getpass import getpass
from pprint import pprint
from time import time
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Functions
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""Generating dictionaries of device creds"""

def devices_detail(devices_info, creds_list):
    devices = {}
    for device_line in devices_info:
        for cred_line in creds_list:
            if device_line[1] == cred_line[0]:  #ip-address matched
                device = {'device_type':device_line[0],'ip':cred_line[0],'username':cred_line[1],'password':cred_line[2]} #per device dict.
        devices[device['ip']] = device  #required. As we cannot append multiple dictionariesin one dictionary. For this we need unique term in above devices which can be used to act as a key to this cumulated dict. In this case, it is ip-address, hence key term is device['ip']
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

def configuring_device(device):
    router_ssh = ConnectHandler(**device)
    if device['device_type'] == 'cisco_ios':
        print('SSH to cisco ios device '+device['ip'])
        write_config(device['device_type'],device['ip'],router_ssh) # calling function write_config()

    if device['device_type'] ==  'cisco_xr':
        print('SSH to cisco XR device '+device['ip'])
        write_config(device['device_type'],device['ip'],router_ssh) # calling function write_config()
    return

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                       MAIN SCRIPT
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

creds_data = input("Enter name of encrypted credentials file (default: encrypted_cred):") or "encrypted_cred"
devices_data = input("Enter name of the devices info file (default: devices_info.csv):") or "devices_info.csv"
password = getpass()
start_time = time() #start time.
devices_raw_data = csv.reader(open(devices_data,'r'))   #reading csv file.
devices_list = [devices_info for devices_info in devices_raw_data]  #creating list from csv file data
pprint("Devices list:\n"+devices_list)
#below json.loads() command converts creds_data.read() bytes data to list which is then decrypted using password as salt
creds_list = json.loads(decrypt(password,open(creds_data,'rb').read()))

devices_info = devices_detail(devices_list,creds_list) #calling function devices_detail()
for [k,v] in devices_info.items():
    configuring_device(v)   #calling function configuring_device()

print('Elapsed time:'+str(time()-start_time)+'sec') #current-time - start-time
