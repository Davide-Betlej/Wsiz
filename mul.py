import time
from datetime import date, datetime
from random import randint

correct = 0
total = 0
liczby_A = []
liczby_B = []
odpowiedzi = []
punkty = []
start=time.time()

for i in range(10):
    a = randint(1,16)
    liczby_A.append(a)
    b = randint(1,16)
    liczby_B.append(b)
    w = input(f'Podaj wynik mnożenia: {a} * {b}:')
    wynik = int(w)  #zamieniamy na liczbę
    odpowiedzi.append(wynik)
    if wynik == a * b:
        print('OK')
        correct += 1
        punkty.append(1)
    else:
        print('Źle')
        punkty.append(0)
    total += 1
    print(f'Wynik dotychczasowy: {correct} / {total} = {correct / total * 100 :.2f} %')
end=time.time()
czas=(end-start)

for i in range(10):
    print('Dla mnożenia liczby:',liczby_A[i], 'z liczbą', liczby_B[i], 'podano wynik:', odpowiedzi[i])
    if punkty[i] == 1:
        print('Odpowiedź była poprawna')
    else:
        print('Odpowiedź była niepoprawna')

print(f'Poprawnych odpowiedzi:', correct)
print (f'Czas: {czas :.2f} s.')

print(f'Czy chcesz zapisać wynik?')
wyb = input(f'y/n?:')
if wyb == 'y':
    plik1 = open('highscore.txt','a', encoding='UTF-8')
    dzis=datetime.now()
    dzis=dzis[:-6]
    plik1.write('\n')
    plik1.write(f'{dzis}')
    for i in range(10):
        plik1.write(f'Dla mnożenia liczby:{liczby_A[i]} z liczbą {liczby_B[i]} podano wynik: {odpowiedzi[i]}')
        plik1.write('\n')
        if punkty[i] == 1:
            plik1.write('Odpowiedź była poprawna')
        else:
            plik1.write('Odpowiedź była niepoprawna')
        plik1.write('\n')
        plik1.write('\n')
    plik1.write(f'Poprawnych odpowiedzi: {correct}')
    plik1.write('\n')
    plik1.write('==================================================================================')
    plik1.write('\n')
    plik1.close()