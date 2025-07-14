dane = open('dane.txt').read()[:-1]

#Zadanie 14.1.
MC1 = {}
for c in range(0, 10):
    MC1[c] = dane.count(str(c))

max_c = max(MC1, key = lambda x: MC1[x])

print(max_c, MC1[max_c])

#Zadanie 14.2.

MC2 = {}

for i in range(len(dane)-10):
    f = dane[i:i+11]
    if not f[0].isdigit() and not f[-1].isdigit() and f[1:-1].isdigit():
        MC2[f[1:-1]] = len(set(f[1:-1]))

min_l_r_c = min(MC2.values())

print('\n'.join(list(filter(lambda x: MC2[x] == min_l_r_c, MC2.keys()))))