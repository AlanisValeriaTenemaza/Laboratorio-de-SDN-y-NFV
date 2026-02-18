import requests

dpid = "0000000000000001"
url = f"http://localhost:8080/firewall/rules/{dpid}"

response = requests.delete(url)

if response.status_code == 200:
    print("Todas las reglas fueron eliminadas correctamente")
else:
    print("Error al eliminar las reglas")
