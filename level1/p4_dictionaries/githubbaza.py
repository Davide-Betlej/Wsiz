import requests
from time import sleep

unikalni1= {}
def recent_logins():
    # zbiera loginname userów 30 ostatnich zdarzeń na github
    r = requests.get('https://api.github.com/events')
    j = r.json()  # to jest tablica słowników/dict
    users = []
    unikalni= {}
    for e in j:
        users.append(e['actor']['login'])
        unikalni[e['actor']['login']] = 1
    return unikalni

for i in range(12):
    unikalni1.update(recent_logins())
    print(unikalni1)
    sleep(10)

print(unikalni1.keys())