czestosc_tekst = {w.split()[0]: int(w.split()[1]) for w in open('czestosc_tekst.txt')}
czestosc = {int(w.split()[1]): w.split()[0] for w in open('czestosc.txt')}
szyfrogram = [w.strip() for w in open('szyfrogram.txt').readlines()]

#Zadanie 4.1.
s = 'CAIMURJH'
s_prim = []

for z in s:
    s_prim.append(czestosc[czestosc_tekst[z]])
print(''.join(s_prim))

#Zadanie 4.2.
zadanie4_2 = open('zadanie4_2.txt', mode='w+')

for w in szyfrogram:
    w_prim = []
    for z in w:
        w_prim.append(czestosc[czestosc_tekst[z]])
    zadanie4_2.write(''.join(w_prim) + '\n')

zadanie4_2.close()