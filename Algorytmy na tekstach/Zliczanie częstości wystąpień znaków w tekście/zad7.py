dane = ''.join([w.strip() for w in open('szachy.txt').readlines() if w != '\n'])

#Wersja toporna

ile_razy_rownowaga1 = 0
min_liczba_bierek1 = 64

for i in range(len(dane) // 64):
    plansza = dane[i * 64:i * 64 + 64]
    TC = [0] * 256
    liczba_bierek = 0
    for b in plansza:
        if b != '.':
            liczba_bierek += 1
            TC[ord(b)] += 1
    czy_rownowaga = True
    for j in range(65, 91):
        if TC[j] != TC[j + 32]:
            czy_rownowaga = False
            break
    if czy_rownowaga:
        ile_razy_rownowaga1 += 1
        if liczba_bierek < min_liczba_bierek1:
            min_liczba_bierek1 = liczba_bierek

print(ile_razy_rownowaga1, min_liczba_bierek1)

#Wersja szybka nr 1

ile_razy_rownowaga2 = 0
min_liczba_bierek2 = 64

for i in range(len(dane) // 64):
    plansza = dane[i * 64:i * 64 + 64]
    biale = []
    czarne = []
    for b in plansza:
        if 65 <= ord(b) <= 90:
            biale.append(b)
        elif 97 <= ord(b) <= 122:
            czarne.append(b.upper())
    biale.sort()
    czarne.sort()
    if biale == czarne:
        ile_razy_rownowaga2 += 1
        min_liczba_bierek2 = min(min_liczba_bierek2, 2 * len(biale))

print(ile_razy_rownowaga2, min_liczba_bierek2)

#Wersja szybka nr 2

ile_razy_rownowaga3 = 0
min_liczba_bierek3 = 64

for i in range(len(dane) // 64):
    plansza = dane[i * 64:i * 64 + 64]
    czy_rownowaga = True
    for a in range(65, 91):
        if plansza.count(chr(a)) != plansza.count(chr(a + 32)):
            czy_rownowaga = False
    if czy_rownowaga:
        ile_razy_rownowaga3 += 1
        liczba_bierek = 64 - plansza.count('.')
        if liczba_bierek < min_liczba_bierek3:
            min_liczba_bierek3 = liczba_bierek

print(ile_razy_rownowaga3, min_liczba_bierek3)