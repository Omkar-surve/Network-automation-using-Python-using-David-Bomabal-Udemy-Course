#!/usr/bin/env python3
from time import time
import csv
#from netmiko import ConnectHandler
#from csv import DictWriter, DictReader
#import simple-crypt
from getpass import getpass
import ipaddress
from pprint import pprint
import threading
from multiprocessing import Pool

def device_details(no_of_devices):
	usernme = input("Enter username to be configured on devices: ")
	passwd = input("Enter password to be configured on devices: ")
	device__type = input("Enter device type (default: cisco_ios): ") or "cisco_ios"
	hostname_prefix = input("Enter hostname prefix to use: ")
	mgmt_ip = input("Enter the mgmt ip/ipv6 pool: ")
	device_port = input("Enter mgmt port name(or default : Ethernet0/0): ") or "Ethernet0/0"
	hostname_list,mgmt_list,mgmt_config = [],[],[]
	for i in range(no_of_devices):
		hostname_list.append(hostname_prefix+str(i))
	return usernme,passwd,mgmt_ip,mgmt_list,hostname_list,device__type,device_port,mgmt_config
	
def ip(IP_pool,no_of_devices,mgmt,mgmt_config):
	ip_pool = ipaddress.ip_network(IP_pool)
	for x in ip_pool.hosts():
	#        while ip_used != str(x):
		ip = ipaddress.ip_address(str(x)).version
		mask = ipaddress.ip_network(IP_pool).netmask
		if ip == 6:
			r_mask = re.search(r"/.*",IP_pool)
			ip_config = "ipv6 address "+str(x)+r_mask.group(0) #o/p: 2001:: mask ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe
			mgmt.append(str(x))
			mgmt_config.append(ip_config)
		else:
			ip_config = "ip address "+str(x)+" "+str(mask) #o/p: 192.168.0.10 mask 255.255.255.254
			mgmt_config.append(ip_config)
			mgmt.append(str(x))
	mgmt_ip_l=[mgmt[n] for n in range(no_of_devices)]
	mgmt_config_l=[mgmt_config[n] for n in range(no_of_devices)]
	return mgmt_ip_l,mgmt_config_l

def hostname_and_mgmt(args):
	usernme,passwd,devices_hostname,mgmt_ip_l,no_of_devices,device__type,device_port,mgmt_config_l=args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7]
	for n in range(no_of_devices):				#for loop starts with new line in file and continues till n-1
		hostnme=devices_hostname[n]
		mgmt_ip=next(mgmt_ip_l)
		mgmt_config=next(mgmt_config_l)
		devices_info_generate_csv(mgmt_ip,hostnme,usernme,passwd,device__type,device_port,no_of_devices,mgmt_config)
	return

def devices_info_generate_csv(mgmt_ip,hostnme,usernme,passwd,device__type,device_port,no_of_devices,mgmt_config):
	with open("devices_info.csv","a") as f:
		csv_writer = csv.DictWriter(f,fieldnames=['device-ip','device_type','hostname','username','password'])
		csv_writer.writerow({
		'device_type':device__type,
		'device-ip':mgmt_ip,
		'hostname':hostnme,
		'username':usernme,
		'password':passwd
		})
	for n in range(no_of_devices):
		with open("Device_initial_config_"+mgmt_ip+".txt","w") as f1:
#			w_output = csv.write(f1)
			with open("SSH_Template.txt","r") as f2:
				output = f2.readlines()
			for i in output:
				i_output = i.format(host=hostnme,password=passwd,username=usernme,mgmt_description="Mgmt link",mgmt_ipv4=mgmt_config)#ip_addr_config[n])#,mgmt_ipv6=mgmt_ipv6)
#				w_output.write(i_output.encode("ascii"))
				f1.write(i_output)#.encode("ascii"))
			#	pprint(n_output)
				continue
	return

##########################################################################################################
"""Main Function"""

no_of_devices = int(input("Enter no. of devices to be configured: "))
usernme,passwd,mgmt_ip,mgmt_list,hostname_list,device__type,device_port,mgmt_config = device_details(no_of_devices)
no_of_threads = Pool(int(input("Enter no. of threads(default 3):") or "3"))
start_time = time()
print("Start time: "+str(start_time)+" sec")
mgmt_ip_l,mgmt_config_l = ip(mgmt_ip,no_of_devices,mgmt_list,mgmt_config)
thread_args = [usernme,passwd,hostname_list,mgmt_ip_l,no_of_devices,device__type,device_port,mgmt_config_l]
no_of_threads.map(hostname_and_mgmt,thread_args)
print("End time: "+str(time())+" sec")
print("Elapsed time: "+str(time()-start_time)+" sec")