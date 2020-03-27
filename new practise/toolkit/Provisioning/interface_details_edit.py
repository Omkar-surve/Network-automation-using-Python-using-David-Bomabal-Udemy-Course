import csv
#from csv import DictWriter, writer, DictReader, reader
from netmiko import ConnectHandler
#from ipaddress import ip_network, ip_address
import ipaddress
import re

def config_devices(router_ssh,ipv4,ipv6,description,port,hostname):
    config_set_list = ['interface '+port,ipv4,ipv6,description]
    output = router_ssh.send_config_set(config_set_list)
    print(output)
    return

def description_generator(remote_hostname,remote_asn,remote_name):
    description = 'description '+remote_hostname+"###"+remote_asn+"###"+remote_name
    return description

def fetch_device_connectivity(Router_1,Router_2):
    with open("device_connectivity.csv","r") as f:
        read_csv = csv.DictReader(f)
        device_list = [Router_1,Router_2]
        for read_line in read_csv:
            for device in device_list:
                if read_line['Router_1'] == Router_1 and read_line['Router_2'] == Router_2:
                    router1_port = read_line['Router1_port']
                    router2_port = read_line['Router2_port']
#        read_csv.close()
    return router1_port, router2_port

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

def config_ip(IP_pool):
    ip_pool = ipaddress.ip_network(IP_pool)
    IP_addr = []
    for x in ip_pool.hosts():
    #        while ip_used != str(x):
        ip = ipaddress.ip_address(str(x)).version
        mask = ipaddress.ip_network(IP_pool).netmask
        if ip == 6:
            r_mask = re.search(r"/.*",IP_pool)
            ip_config = "ipv6 address "+str(x)+r_mask.group(0) #o/p: 2001:: mask ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe
            IP_addr.append(ip_config)
        else:
            ip_config = "ip address "+str(x)+" "+str(mask) #o/p: 192.168.0.10 mask 255.255.255.254
            IP_addr.append(ip_config)
    return IP_addr
#    print(ip_config)    #tobe: used as returning function

######################################################################################################3
Router_1 = input("Router_1 hostname: ") or 'R1'
Router_2 = input("Router_2 hostname: ") or 'R2'
IPv4_pool = input("Input IPv4 pool to use: ") or '12.1.2.0/31'
IPv6_pool = input("Input IPv6 pool to use: ") or '2001:100:300:1:2::/127'
IPv4_pool_list = config_ip(IPv4_pool)
IPv6_pool_list = config_ip(IPv6_pool)
Router_1_port, Router_2_port = fetch_device_connectivity(Router_1,Router_2)
r1_ssh,r1_asn,r1_name = router_ssh_f(Router_1)
#r1_ssh = router_ssh_f(Router_1)
#print(r1_ssh)
r2_ssh,r2_asn,r2_name = router_ssh_f(Router_2)
r1_port_description = description_generator(Router_2,r2_asn,r2_name)
#print(r1_port_description)
r2_port_description = description_generator(Router_1,r1_asn,r1_name)
config_devices(r1_ssh,IPv4_pool_list[0],IPv6_pool_list[0],r1_port_description, Router_1_port,Router_1)
config_devices(r2_ssh,IPv4_pool_list[1],IPv6_pool_list[1],r2_port_description, Router_2_port,Router_2)

#if __name__ == '__main__':
#    main()
