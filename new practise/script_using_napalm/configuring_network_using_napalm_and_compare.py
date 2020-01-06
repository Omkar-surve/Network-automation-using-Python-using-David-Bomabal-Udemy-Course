from napalm import get_network_driver
from pprint import pprint

driver =get_network_driver('ios')
ios = driver('10.10.2.3','omkar','cisco')

ios.open()

ios.load_merge_candidate('IOS_config_using_napalm.txt')
diff = ios.compare_config()
pprint(diff)
