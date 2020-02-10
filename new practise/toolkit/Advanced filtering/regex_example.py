import re
raw_data = []
with open('BGP_neighor_details_for_10.10.2.6','r') as f:
    raw_data = f.read().strip().splitlines()
    
    lastline = raw_data[-1].strip().split()
    print(lastline)
