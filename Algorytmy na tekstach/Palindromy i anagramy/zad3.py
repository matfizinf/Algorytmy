def czy_anagramy2(s1, s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))

dane = [w.split() for w in open('dane_anagramy.txt').readlines()]

#Zadanie 3.1.
ile_w = 0

for w in dane:
    if czy_anagramy2(w[0], w[1]):
        ile_w += 1

print(ile_w)

#Zadanie 3.2.
dane2 = []
for w in dane:
    dane2 += w

ile_max = 0

for l1 in dane2:
    ile = 0
    for l2 in dane2:
        if czy_anagramy2(l1, l2):
            ile += 1
    if ile > ile_max:
        ile_max = ile

print(ile_max)