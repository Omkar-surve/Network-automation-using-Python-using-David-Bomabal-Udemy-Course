from nornir import InitNornir
nr = InitNornir(config_file="config.yaml")

print(nr.inventory.hosts['R1']['site'])
