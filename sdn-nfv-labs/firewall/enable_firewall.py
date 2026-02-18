import requests

dpid = "0000000000000001"
url = f"http://localhost:8080/firewall/module/enable/{dpid}"

requests.put(url)
print("Firewall habilitado")
