import requests

url = 'http://localhost:5000/api'

r = requests.post(url,json={'RestBP':170,})
print(r.json())