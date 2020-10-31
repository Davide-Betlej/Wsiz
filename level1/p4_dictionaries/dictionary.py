m = {}

m['Nowak'] = 90488
m['Kowalska'] = 63003
m['Wiśniewska'] = 49968
m['Wójcik'] = 45041
m['Kowalczyk'] = 44756
m['Kamińska'] = 43032
m['Lewandowska'] = 42678
m['Zielińska'] = 41143
m['Szymańska'] = 40438
m['Woźniak'] = 40269

def surname_count_by_prefix(prefix: str):
    sum = 0
    for k in m.keys():
        if k.startswith(prefix):
            sum += m[k]
    return sum
print(surname_count_by_prefix('K'))
