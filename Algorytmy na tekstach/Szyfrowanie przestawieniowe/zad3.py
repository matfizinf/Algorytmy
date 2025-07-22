dane = [w.strip() for w in open('sygnaly.txt').readlines()]
wynik = []

for i in range(len(dane)):
    if i % 40 == 39:
        wynik.append(dane[i][9])

print(''.join(wynik))