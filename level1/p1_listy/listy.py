w = [1, 0, 8, 2, 5]

print(w)
print(w[0])  # pierwszy elemenet listy
print(w[1])
print(w[-1])  # ostatni element listy

bb = w[1:]  # podlista `w` od elementu 1 do końca
print(bb)

cc = w[1:4] # podlista `w` od elementu nr 1 do elementu 3 włącznie (bez 4)
print(cc)

dd = w[0:-1] # cała lista poza ostatim elementem
print(dd)

for i in range(len(w)):
    print(f'z lewej: {w[i]}, z prawej: {w[-1-i]}')
    if w[i] != w[-1-i]:
        is_ok = False

print(f'lista jest ok? {is_ok}')