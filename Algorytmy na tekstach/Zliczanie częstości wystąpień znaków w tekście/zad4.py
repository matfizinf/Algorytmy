dane1 = [list(map(int, w.split())) for w in open('dane1.txt').readlines()]
dane2 = [list(map(int, w.split())) for w in open('dane2.txt').readlines()]

#Metoda toporna

nr_w1 = 0
l_w1 = 0

for i, (c1, c2) in enumerate(zip(dane1, dane2)):
    TC1 = [0] * 101
    TC2 = [0] * 101

    for l1 in c1:
        if TC1[l1] == 0:
            TC1[l1] += 1
    for l2 in c2:
        if TC2[l2] == 0:
            TC2[l2] += 1

    if TC1 == TC2:
        l_w1 += 1
        nr_w1 = i + 1

print(l_w1, nr_w1)

#Metoda szybka

wynik = [i + 1 for i, (c1, c2) in enumerate(zip(dane1, dane2)) if set(c1) == set(c2)]
print(len(wynik), '\n'.join(list(map(str, wynik))))