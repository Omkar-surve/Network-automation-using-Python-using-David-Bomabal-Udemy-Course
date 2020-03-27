import csv
import time
from csv import reader, DictWriter, writer, DictReader
from netmiko import ConnectHandler
from ipaddress import ip_network, ip_address
#import ipaddress
import re

def router_ssh_f(Router_hostname):
    with open("device_info.csv","r") as f1:
        read_csv1 = csv.DictReader(f1)
        with open("creds.csv","r") as f2:
            read_csv2 = csv.DictReader(f2)
            for read_line1 in read_csv1:
                if read_line1["Hostname"] == Router_hostname:
                    device_line = dict(read_line1)
            for read_line2 in read_csv2:
                if read_line2['Hostname'] == Router_hostname:
                    creds_line = dict(read_line2)
            asn = device_line["ASN"]
            name = device_line["ISP_name"]
            router = {'device_type':device_line["Device-type"],'ip':creds_line["Mgmt"],'username':creds_line["username"],'password':creds_line["password"]}
            router_ssh = ConnectHandler(**router)
            return router_ssh, asn, name

def description_generator(remote_hostname,remote_asn,remote_name):
    description = 'description '+remote_hostname+"###"+remote_asn+"###"+remote_name
    return description


Router_1 = input("Router_1 hostname: ") or 'R1'
Router_2 = input("Router_2 hostname: ") or 'R2'
r1_ssh,r1_asn,r1_name = router_ssh_f(Router_1)
r2_ssh,r2_asn,r2_name = router_ssh_f(Router_2)
r1_port_description = description_generator(Router_2,r2_asn,r2_name)
print(r1_port_description)
r2_port_description = description_generator(Router_1,r1_asn,r1_name)
print(r2_port_description)
#print(r1_ssh)
#print(r2_ssh)
