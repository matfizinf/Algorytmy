tj = [w.strip() for w in open('tj.txt')]
sz = [w.strip() for w in open('sz.txt')]
klucze1 = [w.strip() for w in open('klucze1.txt')]
klucze2 = [w.strip() for w in open('klucze2.txt')]

#Zadanie 2.1.
wynik2a = open('wynik2a.txt', mode='w+')

for t, k1 in zip(tj, klucze1):
    t_prim = []
    j = 0
    for i in range(len(t)):
        if ord(t[i]) + ord(k1[j]) - 64 > 90:
            t_prim.append(chr(ord(t[i]) + ord(k1[j]) - 64 - 26))
        else:
            t_prim.append(chr(ord(t[i]) + ord(k1[j]) - 64))
        j += 1
        if j >= len(k1):
            j = 0
    wynik2a.write(''.join(t_prim) + '\n')

wynik2a.close()

#Zadanie 2.2.
wynik2b = open('wynik2b.txt', mode='w+')
for s, k2 in zip(sz, klucze2):
    s_prim = []
    j = 0
    for i in range(len(s)):
        if ord(s[i]) - (ord(k2[j]) - 64) < 65:
            s_prim.append(chr(ord(s[i]) - (ord(k2[j]) - 64) + 26))
        else:
            s_prim.append(chr(ord(s[i]) - (ord(k2[j]) - 64)))
        j += 1
        if j >= len(k2):
            j = 0
    wynik2b.write(''.join(s_prim) + '\n')

wynik2b.close()