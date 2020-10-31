import requests
from time import sleep

def recent_logins():
    # zbiera loginname userów 30 ostatnich zdarzeń na github
    r = requests.get('https://api.github.com/events')
    j = r.json()  # to jest tablica słowników/dict
    users = []
    for e in j:
        users.append(e['actor']['login'])
    return users

for i in range(12):
    users = recent_logins()
    users.append(users)
    print(users)
    sleep(10)

unikalna_lista = []
for item in users:
    if item not in unikalna_lista:
        unikalna_lista.append(item)

print('Unikalne loginy pomyślnie zapisane w pliku loginy.txt')
print(f'Liczba unikalnych loginów:{len(unikalna_lista)}')

plik1 = open('loginy.txt', 'a', encoding='UTF-8')
plik1.write(f'Twoja unikalna lista to: {item}')
plik1.close