w = [1, 2, 3, 5, 1, 3, 4]
sumakwadratow = 0
suma = 0
lista2 = sorted(w)
print(f'Lista:{w}')
print(f'Ułożona lista:{lista2}')
for i in w:
    suma += i
    sumakwadratow = suma + i**2
print(f'Suma listy to:{suma}')
print (f'Suma kwadratów listy to: {sumakwadratow}') #A
print(f'Największym elementem listy jest: {lista2[-1]}') #B

