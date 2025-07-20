#Zadanie 3.1.
dane_6_1 = list(map(lambda x: x.strip(), open('dane_6_1.txt').readlines()))
wynik_3_1 = open('wynik_3_1.txt', mode='w+')

for s in dane_6_1:
    s_prim = []
    for i in range(len(s)):
        s_prim.append(chr(ord(s[i]) + 107 % 26 if ord(s[i]) + 107 % 26 <= 90 else ord(s[i]) + 107 % 26 - 26))
    wynik_3_1.write(f"{''.join(s_prim)}\n")
wynik_3_1.close()

#Zadanie 3.2.
dane_6_2 = list(map(lambda x: [x.split()[0], int(x.split()[1])], open('dane_6_2.txt').readlines()[:700]))
wynik_3_2 = open('wynik_3_2.txt', mode='w+')

for p in dane_6_2:
    s_prim = []
    for i in range(len(p[0])):
        s_prim.append(chr(ord(p[0][i]) - p[1] % 26 if ord(p[0][i]) - p[1] % 26 >= 65 else ord(p[0][i]) - p[1] % 26 + 26))
    wynik_3_2.write(f"{''.join(s_prim)}\n")
wynik_3_2.close()

#Zadanie 3.3.
dane_6_3 = list(map(lambda x: x.split(), open('dane_6_3.txt').readlines()))
wynik_3_3 = open('wynik_3_3.txt', mode='w+')

for p in dane_6_3:
    if ord(p[0][0]) < ord(p[1][0]):
        k = ord(p[1][0]) - ord(p[0][0])
    else:
        k = ord(p[1][0]) - ord(p[0][0]) + 26
    for i in range(len(p[0])):
        if ord(p[0][i]) < ord(p[1][i]):
            k_prim = ord(p[1][i]) - ord(p[0][i])
        else:
            k_prim = ord(p[1][i]) - ord(p[0][i]) + 26
        if k != k_prim:
            wynik_3_3.write(p[0] + '\n')
            break
wynik_3_3.close()