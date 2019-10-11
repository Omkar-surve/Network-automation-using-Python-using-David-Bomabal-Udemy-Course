#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os
from pprint import pprint

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    json_text = file.read()
#    print("JSON data type is ",type(json_text))    trial
#    pprint(json_text)                              trail
    json_data = json.loads(json_text)
#    print("JSON Python native data type is ",type(json_data))             trail
#    pprint(json_data)              trail
    for n in range(0,3):
        inet_name = json_data['ietf-interfaces:interfaces']['interface'][n]['name']
        inet_ip = json_data['ietf-interfaces:interfaces']['interface'][n]['ietf-ip:ipv4']['address'][0]['ip']
        inet_ip_mask = json_data['ietf-interfaces:interfaces']['interface'][n]['ietf-ip:ipv4']['address'][0]['netmask']
        print("name:",inet_name,"| ip:",inet_ip,"| mask:",inet_ip_mask,"\n")
#        print("ip:",inet_ip)                   trail
#        print(inet_ip_mask,"\n")               trail

# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.
