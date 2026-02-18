import requests
import json

dpid = "0000000000000001"
url = f"http://localhost:8080/firewall/rules/{dpid}"

data = {
    "nw_src": "10.0.0.1/32",
    "nw_dst": "10.0.0.2/32",
    "nw_proto": "ICMP"
}

headers = {"Content-Type": "application/json"}
requests.post(url, data=json.dumps(data), headers=headers)

print("Regla ICMP agregada")

