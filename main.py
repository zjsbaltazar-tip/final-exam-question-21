import json
import requests
requests.packages.urllib3.disable_warnings()

LASTNAME = "BALTAZAR"
USERNAME = "cisco"
PASSWORD = "cisco123!"

api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = (USERNAME, PASSWORD)

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet1",
        "description": "VBox",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.168.56.101",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))

#Hostname

api_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/hostname"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = (USERNAME, PASSWORD)

yangConfig = {
    "Cisco-IOS-XE-native:hostname": LASTNAME
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))