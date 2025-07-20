dokad = open('dokad.txt').read()
szyfr = [w.strip() for w in open('szyfr.txt').readlines()]

Vigenere_wyniki = open('Vigenere_wyniki.txt', mode='w+')

#Zadanie 8.1.
klucz = 'LUBIMYCZYTAC'
dokad_prim = []
ile_powtorzen_klucza = 1

j = 0
for z in dokad:
    if j >= len(klucz):
        ile_powtorzen_klucza += 1
        j = 0
    if ord(z) in range(65, 91):
        k = ord(klucz[j]) - 65
        if ord(z) + k > 90:
            dokad_prim.append(chr(ord(z) + k - 26))
        else:
            dokad_prim.append(chr(ord(z) + k))
        j += 1
    else:
        dokad_prim.append(z)

Vigenere_wyniki.write(f"{ile_powtorzen_klucza}\n{''.join(dokad_prim)}\n")

#Zadanie 8.2.
tekst_zaszyfrowany = szyfr[0]
klucz = szyfr[1]
tekst_zaszyfrowany_prim = []

j = 0
for z in tekst_zaszyfrowany:
    if j >= len(klucz):
        j = 0
    if ord(z) in range(65, 91):
        k = ord(klucz[j]) - 65
        if ord(z) - k < 65:
            tekst_zaszyfrowany_prim.append(chr(ord(z) - k + 26))
        else:
            tekst_zaszyfrowany_prim.append(chr(ord(z) - k))
        j += 1
    else:
        tekst_zaszyfrowany_prim.append(z)

Vigenere_wyniki.write(f"{''.join(tekst_zaszyfrowany_prim)}\n")

#Zadanie 8.3.
czestosc_znakow = {}

for z in tekst_zaszyfrowany:
    if ord(z) in range(65, 91):
        if z in czestosc_znakow:
            czestosc_znakow[z] += 1
        else:
            czestosc_znakow[z] = 1

n = sum(czestosc_znakow.values())
suma = 0

for a in range(65, 91):
    Vigenere_wyniki.write(f'{chr(a)} - {czestosc_znakow[chr(a)]}\n')
    suma += czestosc_znakow[chr(a)] * (czestosc_znakow[chr(a)] - 1)

K0 = suma / (n * (n - 1))
d = 0.0285 / (K0 - 0.0385)

Vigenere_wyniki.write(f'{len(szyfr[1])} {round(d, 2)}')

Vigenere_wyniki.close()