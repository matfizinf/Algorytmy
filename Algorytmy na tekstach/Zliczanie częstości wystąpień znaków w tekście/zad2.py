dane = [w.split() for w in open('punkty.txt').readlines()]

#Wersja toporna

wynik1 = 0

for p in dane:
    TCx = [0] * 256
    TCy = [0] * 256

    for i in range(len(p[0])):
        if TCx[ord(p[0][i])] == 0:
            TCx[ord(p[0][i])] += 1

    for j in range(len(p[1])):
        if TCy[ord(p[1][j])] == 0:
            TCy[ord(p[1][j])] += 1

    if TCx == TCy:
        wynik1 += 1

print(wynik1)

#Wersja szybka

wynik2 = sum([1 for p in dane if set(p[0]) == set(p[1])])

print(wynik2)