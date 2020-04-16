#!/usr/bin/env python3
from csv import DictWriter,DictReader,reader

class write_list:
	def write_list(ip):
		with open("used_ip_list.csv","r") as f1:
			read_line = csv.Dictreader(f1)
			if line['mgmt-ip'] != ip:
				with open("used_ip_list.csv","a") as f2:
					write_line = csv.DictWriter(f2,fieldnames=['mgmt-ip'])
					csv_writer.writerow({'mgmt-ip':ip})
				return True
