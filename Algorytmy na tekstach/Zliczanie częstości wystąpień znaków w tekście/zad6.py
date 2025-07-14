dane = [w.split() for w in open('instrukcje.txt').readlines()]

#Metoda toporna

max_z_d = ''
max_l_d = 0
TC = [0] * 256

for p in dane:
    if p[0] == 'DOPISZ':
        TC[ord(p[1])] += 1
        if TC[ord(p[1])] > max_l_d:
            max_l_d = TC[ord(p[1])]
            max_z_d = p[1]

print(max_z_d, max_l_d)

#Metoda szybka

litery_dopisywane = [p[1] for p in dane if p[0] == 'DOPISZ']
litery_dopisywane2 = litery_dopisywane.copy()
litery_dopisywane2.sort(key = lambda x: -litery_dopisywane.count(x))
print(litery_dopisywane2[0], litery_dopisywane2.count(litery_dopisywane2[0]))