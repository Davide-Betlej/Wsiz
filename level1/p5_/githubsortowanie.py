import requests

r = requests.get('https://api.github.com/events')
j = r.json()

p = sorted(j, key=lambda a:a['actor']['login'])

for i in p:
    print(i['actor'])