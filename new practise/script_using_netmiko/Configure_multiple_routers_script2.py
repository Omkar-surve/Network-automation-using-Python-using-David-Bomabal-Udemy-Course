#importing function named ConnectHandler from module named netmiko
from netmiko import ConnectHandler

#defining routers parameters in definition.
AS100_R1 = {'device_type':'cisco_ios','ip':'10.10.2.1','username':'omkar','password':'cisco'}
AS300_R2 = {'device_type':'cisco_ios','ip':'10.10.2.2','username':'omkar','password':'cisco'}
AS400_R3 = {'device_type':'cisco_ios','ip':'10.10.2.3','username':'omkar','password':'cisco'}
AS400_R4 = {'device_type':'cisco_ios','ip':'10.10.2.4','username':'omkar','password':'cisco'}
AS200_R5 = {'device_type':'cisco_xr','ip':'10.10.2.5','username':'omkar','password':'cisco'}
AS500_R6 = {'device_type':'cisco_xr','ip':'10.10.2.6','username':'omkar','password':'cisco'}

#Creating list of defined objects above.
all_routers = [AS100_R1,AS300_R2,AS400_R3,AS400_R4,AS200_R5,AS500_R6]

#For each router in the list named all_routers send command in 'send_command'
for router in all_routers:
    #ConnectHandler ssh into router with parameters defined.
    router_ssh = ConnectHandler(**router)
    #print line
    print('='*80)
    # object 'output' stores the output of send_command function send to object router_ssh.
    output = router_ssh.send_command('show ip int br')
    #print output.
    print (output)
    #print line.
    print('='*80)
