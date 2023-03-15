import requests
import urllib3

urllib3.disable_warnings()

host = "https://10.10.11.133:8443/"
headers = {'Content-Type':'application/json'}

req = requests.get(host, verify=False)
res = req.text

print(res)
