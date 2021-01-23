import json
import urllib3
from tabulate import tabulate

http = urllib3.PoolManager()
response = http.request('GET','http://ipinfo.io/json')
data = json.load(response)

table = [
    ["IP-Adress:", data["ip"]],
    ["Server:", data["org"]],
    ["City:", data["city"]],
    ["Country:", data["country"]],
    ["Region:", data["region"]]
]

print(tabulate(table))
