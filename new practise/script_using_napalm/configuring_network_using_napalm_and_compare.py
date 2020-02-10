from napalm import get_network_driver
from pprint import pprint
from netmiko import ConnectHandler
from simplecrypt import encrypt, decrypt
import json
import csv
from getpass import getpass
from time import time
import threading
from multiprocessing import Pool

#for cisco 'ios' support available for v12 only.
#for cisco 'ios' we need 'ip scp server enable'
#for cisco 'xr' we need 'xml agent tty iteration off'
#!/usr/bin/env python
"""Encrypting and Decrypting contents of the file using JSON"""

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

def write_config(device,device_type,device_ip):
    print(">>>>>>>>>>Copying config of router "+device_ip)
    device.open()
    if device_type == 'cisco_ios':
        with open('Cisco_IOS_config_backup_for_'+device_ip,'w') as f:
            output = device.get_config()
            f.write(str(output))
        device.close()
    if device_type == 'cisco_xr':
        with open('Cisco_XR_config_backup_for_'+device_ip,'w') as f:
            output = device.get_config()
            f.write(str(output))
        device.close()
    return

def configuring_device(dev_list):
    dev = dev_list
    if dev[0] == 'cisco_ios':
        driver = get_network_driver('ios')
        device = driver(dev[1],dev[2],dev[3])
        write_config(device,dev[0],dev[1])
    if dev[0] == 'cisco_xr':
        driver = get_network_driver('iosxr')
        device = driver(dev[1],dev[2],dev[3])
        print('Device: '+dev[1])
        try:
            print(str(device.get_bgp_neighbors()))
        except:
            print('get_facts() method not supported in XR')
        write_config(device,dev[0],dev[1])
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
#thread_list = []

new_device_list = []
devices_info = devices_detail(devices_list,creds_list)
for [k,v] in devices_info.items():
    new_device_list.append((v['device_type'],v['ip'],v['username'],v['password']))
no_of_threads.map(configuring_device,new_device_list)
print('Elapsed time:'+str(time()-start_time)+'sec')
#####################################################################################################################3
