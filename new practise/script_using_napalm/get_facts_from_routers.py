from napalm import get_network_driver #importing network driver class in napalm library
from pprint import pprint

driver = get_network_driver('iosxr')    #loading get_network_driver function with args 'iosxr'
cisco_ios = driver('10.10.2.5','omkar','cisco') #passing credentials
cisco_ios.open()    #ssh connection to devices

output = cisco_ios.get_bgp_neighbors()  #passing show commands

pprint(output)  # print output
