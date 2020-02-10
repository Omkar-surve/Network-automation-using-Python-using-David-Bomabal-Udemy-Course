from pprint import pprint
import json
from urllib.request import Request, urlopen
req = Request('https://cmxlocationsandbox.cisco.com/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
response = urlopen(req)
response_string = response.read().decode('utf-8')
response_string_json = json.loads(response_string)
#pprint(response_string_json )
for detail in response_string_json['accessPoints']:
    print("Accesspoint name:",detail['name'],'mac:',detail['radioMacAddress'])#, '\tip:',detail['ipAddress'],"\n")
#print(json.dumps(response_string_json, sort_keys=False, indent=2))
response.close()
