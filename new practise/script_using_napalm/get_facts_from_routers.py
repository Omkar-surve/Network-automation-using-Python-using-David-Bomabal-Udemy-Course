from napalm import get_network_driver #importing network driver class in napalm library
from pprint import pprint
<<<<<<< HEAD
from time import time
import json
=======
>>>>>>> a5697e3139c217d5cf11781e7f4da928da21ddcb

driver = get_network_driver('iosxr')    #loading get_network_driver function with args 'iosxr'
cisco_ios = driver('10.10.2.5','omkar','cisco') #passing credentials
cisco_ios.open()    #ssh connection to devices
<<<<<<< HEAD
start_time = time()

output = json.dumps(cisco_ios.get_facts(), indent=4)  #passing show commands

pprint(output)  # print output
print('Elapsed time:'+str(time()-start_time)+'sec')
=======

output = cisco_ios.get_bgp_neighbors()  #passing show commands

pprint(output)  # print output
>>>>>>> a5697e3139c217d5cf11781e7f4da928da21ddcb
