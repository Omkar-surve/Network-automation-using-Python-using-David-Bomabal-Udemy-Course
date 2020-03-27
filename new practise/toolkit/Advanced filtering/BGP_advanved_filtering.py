"""Encrypting and Decrypting contents of the file using JSON"""
from netmiko import ConnectHandler
from simplecrypt import encrypt, decrypt
import json
import csv
from tool import bgp_summary_tool
from getpass import getpass
from pprint import pprint
from time import time
import threading
from multiprocessing import Pool
import re
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

def bgp_summary(device_type,device_ip,router_ssh):
    print(">>>>>>>>>Show bgp summary on "+device_ip)
    show_commands = ['show bgp ipv4 unicast summary | b Neighbor']#,'show bgp ipv6 unicast summary | b Neighbor']
    for show_command in show_commands:
        output = router_ssh.send_command(show_command)
        data, header = bgp_summary_tool.bgp_summary_filtering(output,device_type,device_ip)
    return data, header


def configuring_device(dev_list):
    dev = tuple(dev_list)
    device = {'device_type':dev[0],'ip':dev[1],'username':dev[2],'password':dev[3]}
    router_ssh = ConnectHandler(**device)
    if device['device_type'] == 'cisco_ios':
        print('SSH to cisco ios device '+device['ip'])
        data_1, header = bgp_summary(device['device_type'],device['ip'],router_ssh)
    if device['device_type'] ==  'cisco_xr':
        print('SSH to cisco XR device '+device['ip'])
        data_1, header = bgp_summary(device['device_type'],device['ip'],router_ssh)
    return bgp_summary_tool.bgp_summary_report_update(data_1,header)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                       MAIN SCRIPT
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

creds_data = input("Enter name of encrypted credentials file (default: encrypted_cred):") or "encrypted_cred"
devices_data = input("Enter name of the devices info file (default: devices_info.csv):") or "devices_info.csv"
password = getpass()
no_of_threads = Pool(int(input("Enter no. of threads(default 3):") or "3"))
command = input("BGP summary:") or "Yes"
if command == "Yes":
    bgp_summary_tool.bgp_add_header("BGP summary")
else:
    pass
start_time = time()
#below json.loads() command converts encrypted_cred_read.read() bytes data to list which is then decrypted using password as salt
devices_raw_data = csv.reader(open(devices_data,'r'))
devices_list = [devices_info for devices_info in devices_raw_data]
pprint(devices_list)
print("total device count:"+str(len(devices_list)))
#below json.loads() command converts encrypted_cred_read.read() bytes data to list which is then decrypted using password as salt
creds_list = json.loads(decrypt(password,open(creds_data,'rb').read()))
new_device_list = []
devices_info = devices_detail(devices_list,creds_list)
for [k,v] in devices_info.items():
    new_device_list.append((v['device_type'],v['ip'],v['username'],v['password']))
no_of_threads.map(configuring_device,new_device_list)

print('Elapsed time:'+str(time()-start_time)+'sec')
