from netmiko import ConnectHandler
from pprint import pprint
class directories_check:
    """
This is a class used to check free space in network devices.
Lets get started.
    """
    def __init__(self,devices):
        ip = devices
        print("Device details:\n"+ip['device_type']+' '+ip['ip']+'\n')
        return
    def login_ssh(ip):
        router_ssh = ConnectHandler(**ip)
        output = router_ssh.send_command('dir').split('\n')
        return output
    def space_check(output):
        last_line = output[-1]
        last_line_list = last_line.strip().split()
        for every_word in last_line_list:
            if every_word.isnumeric():
                total_space = ""
                total_space = every_word
            if ')' and '(' in every_word:
                if every_word[1:-1].isnumeric():
                    free_space = every_word[1:]

        return free_space,total_space
