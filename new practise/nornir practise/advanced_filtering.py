from nornir import InitNornir
from nornir.core.filter import F
nr = InitNornir(config_file="config.yaml")

#print(nr.inventory.hosts)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#           Using Filter function
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#           Using Filter Object
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""Print routers with specific as numbers"""
asnn = nr.filter(F(asn__contains="400"))
print(asnn.inventory.hosts.keys())
