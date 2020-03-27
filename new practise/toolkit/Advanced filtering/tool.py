from csv import DictWriter,writer
import re
from pprint import pprint
import time

class BGPTool:
    """
    This class performes BGP neighbor summary, BGP route check, advertised route count.
    """
class bgp_summary_tool:
    def bgp_add_header(command):
        with open(command+" report","w") as r:
            csv_writer = DictWriter(r, fieldnames=['Device Mgmt IP','Neighbor', 'V', 'AS', 'MsgRcvd', 'MsgSent', 'TblVer', 'InQ', 'OutQ', 'Up/Down', 'State/PfxRcd'])
#            csv_writer = DictWriter(f, fieldnames=header_list)
#above commented command donot work because filednames gets sorted in ascending order of the values in list
            csv_writer.writeheader()
        return
    def bgp_summary_report_update(data_v,header_list):
        with open("BGP summary report","a") as f:
            csv_writer = DictWriter(f, fieldnames=['Device Mgmt IP','Neighbor', 'V', 'AS', 'MsgRcvd', 'MsgSent', 'TblVer', 'InQ', 'OutQ', 'Up/Down', 'State/PfxRcd'])
            for n in range(0,len(data_v)):
                data_wr = data_v[n]
                for i in range(0,len(data_wr)):
                    a_dict={
                        'Device Mgmt IP' : data_wr[0],
                        'Neighbor' : data_wr[1],
                        'V' : data_wr[2],
                        'AS' : data_wr[3],
                        'MsgRcvd' : data_wr[4],
                        'MsgSent' : data_wr[5],
                        'TblVer' : data_wr[6],
                        'InQ' : data_wr[7],
                        'OutQ' : data_wr[8],
                        'Up/Down' : data_wr[9],
                        'State/PfxRcd' : data_wr[10]
                            }
                csv_writer.writerow(a_dict)
        return
    def bgp_summary_filtering(output,device_type,device_ip):
        raw_data = output.strip().splitlines()
        header_list = []
        if device_type == 'cisco_xr':
            k = 1
        else: k = 0
        data_csv = []
        for n in range(k,len(raw_data)):
            match_header = re.search(r"^Neighbor .*",raw_data[n])
            if match_header:
                header_list.insert(0,'Device Mgmt IP')
                header_list = match_header.group(0).strip().split()
            matched_output = re.search(r"\d+\D+\d+.*",raw_data[n])
            if matched_output:
                neighbor_list = []
                neighbor_list.insert(0,device_ip)
                neighbor_list.extend(matched_output.group(0).strip().split())
                data_csv.append(neighbor_list)
            else:
                pass
        return data_csv,header_list


"""PROBLEM: need to define dictionary for each entry or loop for each dictionary"""
"""SOLUTION: using pandas module"""
