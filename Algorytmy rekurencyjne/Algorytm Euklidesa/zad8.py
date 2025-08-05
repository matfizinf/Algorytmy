dane = [list(map(int, w.split())) for w in open('rozklady.txt').readlines()]

minima_czynnikow = {}
for c in dane[0]:
    if c in minima_czynnikow:
        minima_czynnikow[c] += 1
    else:
        minima_czynnikow[c] = 1

for l in dane:
    for c in minima_czynnikow:
        if l.count(c) < minima_czynnikow[c]:
            minima_czynnikow[c] = l.count(c)

nwd = 1

for c in minima_czynnikow:
    nwd *= minima_czynnikow[c] * c

print(nwd)