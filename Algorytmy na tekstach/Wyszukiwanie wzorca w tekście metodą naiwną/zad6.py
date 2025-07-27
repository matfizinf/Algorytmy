dane = [w.strip() for w in open('symbole.txt').readlines()]

ile = 0
srodki = []

for i in range(1, len(dane) - 1):
    for j in range(1, len(dane[0]) - 1):
        symbol = dane[i][j]
        czy_prostokat = True
        for k in range(-1, 2):
            for l in range(-1, 2):
                if dane[i + k][j + l] != symbol:
                    czy_prostokat = False
        if czy_prostokat:
            ile += 1
            srodki += [i + 1, j + 1]

print(ile, ' '.join(list(map(str, srodki))))