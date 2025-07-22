dane = [w.strip() for w in open('napisy.txt').readlines()]

#Zadanie 5.1.
for i in range(19, len(dane), 20):
    print(dane[i][i // 20], end='')
print()

#Zadanie 5.2.
#Sposób 1
pomocnicza = [''.join(list(filter(lambda x: x.isdigit(), w))) for w in dane]
pomocnicza = ''.join([w[:len(w)-len(w)%2] for w in pomocnicza])
wynik = ''

for i in range(0, len(pomocnicza), 2):
    kod = int(pomocnicza[i:i+2])
    if 65 <= kod <= 90:
        wynik += chr(kod)

print(wynik[:wynik.find('XXX')+3])

#Sposób 2 (Różni się od 1 sposobem konstrukcji listy "pomocnicza")
pomocnicza = ''
for w in dane:
    for z in w:
        if z.isdigit():
            pomocnicza += z
    if len(pomocnicza) % 2 == 1:
        pomocnicza = pomocnicza[:-1]

for i in range(0, len(pomocnicza), 2):
    kod = int(pomocnicza[i:i+2])
    if 65 <= kod <= 90:
        wynik += chr(kod)

print(wynik[:wynik.find('XXX')+3])