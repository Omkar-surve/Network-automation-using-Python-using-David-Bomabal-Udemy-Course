#!/usr/bin/env python3
import concurrent.futures
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
	mgmt_list,mgmt_config = [],[]
	# for i in range(no_of_devices):
	# 	hostname_list.append(hostname_prefix+str(i))
	hostname_list = (hostname_prefix+str(i) for i in range(no_of_devices))
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
	mgmt_ip_l=(mgmt[n] for n in range(no_of_devices))
	mgmt_config_l=(mgmt_config[n] for n in range(no_of_devices))
	return mgmt_ip_l,mgmt_config_l

def hostname_and_mgmt(usernme,passwd,hostname_list,mgmt_ip_l,no_of_devices,device__type,device_port,mgmt_config_l):
	list_iterations = []
	device_details_iteration = []
	for n in range(no_of_devices):			#for loop starts with new line in file and continues till n-1
#		host_name=next(hostname_list)
		mgmt_ip=next(mgmt_ip_l)
		mgmt_config=next(mgmt_config_l)
		device_details_iteration=[mgmt_ip,next(hostname_list),usernme,passwd,device__type,device_port,no_of_devices,mgmt_config]
		list_iterations.append(device_details_iteration)
	with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
#	thread_args = hostname_and_mgmt(usernme,passwd,hostname_list,mgmt_ip_l,no_of_devices,device__type,device_port,mgmt_config_l)
		results=executor.map(devices_info_generate_csv,list_iterations)

	return results#list_iterations

def devices_info_generate_csv(values):
#	print(values)

# #	device_details_iteration =[]
# 	for device_details_iteration in list_iterations:
# 		print(type(list_iterations))
	mgmt_ip,host_name,usernme,passwd,device__type,device_port,no_of_devices,mgmt_config=values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7]
	with open("devices_info.csv","a") as f:
		csv_writer = csv.DictWriter(f,fieldnames=['device-ip','device_type','hostname','username','password'])
		csv_writer.writerow({
		'device_type':device__type,
		'device-ip':mgmt_ip,
		'hostname':host_name,
		'username':usernme,
		'password':passwd
		})
	for n in range(int(no_of_devices)):
		with open("Device_initial_config_"+mgmt_ip+".txt","w") as f1:
#			w_output = csv.write(f1)
			with open("SSH_Template.txt","r") as f2:
				output = f2.readlines()
			for i in output:
				i_output = i.format(host=host_name,password=passwd,username=usernme,mgmt_description="Mgmt link",mgmt_ipv4=mgmt_config)#ip_addr_config[n])#,mgmt_ipv6=mgmt_ipv6)
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
#values = thread_args
#print(thread_args)
# with concurrent.futures.ProcessPoolExecutor() as executor:
# 	thread_args = hostname_and_mgmt(usernme,passwd,hostname_list,mgmt_ip_l,no_of_devices,device__type,device_port,mgmt_config_l)
# 	results=executor.map(devices_info_generate_csv,thread_args)
#no_of_threads.map(devices_info_generate_csv,values)

hostname_and_mgmt(usernme,passwd,hostname_list,mgmt_ip_l,no_of_devices,device__type,device_port,mgmt_config_l)
print("End time: "+str(time())+" sec")
print("Elapsed time: "+str(time()-start_time)+" sec")