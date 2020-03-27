import re
from pprint import pprint
from time import time

start_time = time()
with open('BGP_neighor_details_for_10.10.2.2','r') as f:
    raw_data = f.read().strip().splitlines()
for n in range(0,len(raw_data)):
    output = re.search(r"\d+\D+\d+.*",raw_data[n])
    if output:
        print(output.group(0).strip().split())
    else:
        pass

print(str(time()-start_time)+" sec")
