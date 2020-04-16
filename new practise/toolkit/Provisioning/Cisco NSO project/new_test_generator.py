ip_list = ['10.10.3.1',
 '10.10.3.2',
 '10.10.3.3',
 '10.10.3.4',
 '10.10.3.5',
 '10.10.3.6',
 '10.10.3.7',
 '10.10.3.8',
 '10.10.3.9',
 '10.10.3.10']


#for loop example:
# for n in ip_list:
# 	mgmt_ip_l.append(n)

#generator example:
def hello(ip_list):
	mgmt_ip_l=[]
	for n in ip_list:
		mgmt_ip_l.append(n)
	yield mgmt_ip_l

hi = hello(ip_list)
print(help(hi))
# for i in hi:
#  	print(i)
#mgmt_ip_l = []

