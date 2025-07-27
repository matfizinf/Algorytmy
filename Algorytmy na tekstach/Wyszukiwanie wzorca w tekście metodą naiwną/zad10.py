dane = [[[0 for _ in range(20)] for _ in range(20)] for _ in range(200)]

plik = open('dane_obrazki.txt')

for i in range(200):
    for j in range(20):
        wiersz = plik.readline().strip()
        for k in range(20):
            dane[i][j][k] = wiersz[k]
    plik.readline()
    plik.readline()

ile = 0

for i in range(200):
    ile_ok = 0
    for j in range(10):
        for k in range(10):
            if dane[i][j + 10][k] == dane[i][j][k] and dane[i][j][k + 10] == dane[i][j][k] and \
                dane[i][j + 10][k + 10] == dane[i][j][k]:
                ile_ok += 1
    if ile_ok == 100:
        ile += 1
        if ile == 1:
            for j in range(20):
                for k in range(20):
                    print(dane[i][j][k], end='')
                print()
print(ile)