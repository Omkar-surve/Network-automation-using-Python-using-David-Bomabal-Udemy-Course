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
    if router == AS100_R1:
        print('Configuring BGP for router '+router['ip'])
        print('='*80)
        f = open('R1.txt','r')
        command_line = f.read().splitlines()
        output = router_ssh.send_config_set(command_line)
        print (output)
        f.close()        #closing opened file.
        print('='*80)
    if router == AS300_R2:
        print('Configuring BGP for router '+router['ip'])
        print('='*80)
        f = open('R2.txt','r')
        command_line = f.read().splitlines()
        output = router_ssh.send_config_set(command_line)
        print (output)
        f.close()        #closing opened file.
        print('='*80)
    if router == AS400_R3:
        print('Configuring BGP for router '+router['ip'])
        print('='*80)
        f = open('R3.txt','r')
        command_line = f.read().splitlines()
        output = router_ssh.send_config_set(command_line)
        print (output)
        f.close()        #closing opened file.
        print('='*80)
    if router == AS400_R4:
        print('Configuring BGP for router '+router['ip'])
        print('='*80)
        f = open('R4.txt','r')
        command_line = f.read().splitlines()
        output = router_ssh.send_config_set(command_line)
        print (output)
        f.close()        #closing opened file.
        print('='*80)
    if router == AS200_R5:
        print('Configuring BGP for router '+router['ip'])
        print('='*80)
        f = open('R5.txt','r')
        command_line = f.read().splitlines()
        output = router_ssh.send_config_set(command_line)
        print (output)
        f.close()  #closing opened file.
        print('='*80)
    if router == AS500_R6:
        print('Configuring BGP for router '+router['ip'])
        print('='*80)
        f = open('R6.txt','r')
        command_line = f.read().splitlines()
        output = router_ssh.send_config_set(command_line)
        print (output)
        f.close()
        print('='*80)

for router in all_routers:
        router_ssh = ConnectHandler(**router)
        print('Router '+router['ip']+' :')
        output = router_ssh.send_command('show bgp ipv4 unicast summary')
        print (output) #print output of show commands.
        print('='*80)
