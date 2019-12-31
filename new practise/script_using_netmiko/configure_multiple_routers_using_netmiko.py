#importing function named ConnectHandler from module named netmiko
from netmiko import ConnectHandler

#defining router R4 parameters in definition AS400_R4
AS400_R4 = {'device_type':'cisco_ios','ip':'10.10.2.4','username':'omkar','password':'cisco'}

#ConnectHandler ssh into router R4 with parameters defined above
router_ssh = ConnectHandler(**AS400_R4)

# object 'output' stores the output of send_command function send to object router_ssh.
output = router_ssh.send_command('show ip int br')

#print object output.
print (output)

#list of commands that will be send to the router.
router_config = ['router ospf 10', 'network 0.0.0.0 0.0.0.0 area 0']
#commands send to the router using function 'send_config_set'.
output = router_ssh.send_config_set(router_config)
#print object output.
print(output)
