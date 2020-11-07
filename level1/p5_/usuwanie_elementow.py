from datetime import datetime


def ts():
    return datetime.now().timestamp()

n = 4 * 10**5
w = [i for i in range(n)]
# print(w)

st = ts()

#usuwanie z przodu
# for i in range(n):
#     del w[0]

#usuwanie z tyłu
for i in range(n):
    del w[len(w)-1]
en = ts()
print(f' Czas wykonania: {(en-st)*1000:.3f}ms')