#!/usr/bin/env python3.6

from pprint import pprint
with open("SSH_Template.txt","r") as f:
	output = f.readlines()
	for n in output:
		n_output = n.format(host="R1",password="cisco",username="omkar")
		pprint(n_output)
		continue