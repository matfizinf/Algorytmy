dane = [w.strip() for w in open('symbole.txt').readlines()]

def napis_na_liczbe10(napis):
    napis_prim = []
    for z in napis:
        if z == 'o':
            napis_prim.append('0')
        elif z == '+':
            napis_prim.append('1')
        else:
            napis_prim.append('2')
    return int(''.join(napis_prim), 3)

def liczba10_na_napis(liczba10):
    wynik = []
    while liczba10 > 0:
        cyfra = liczba10 % 3
        if cyfra == 0:
            wynik.append('o')
        elif cyfra == 1:
            wynik.append('+')
        else:
            wynik.append('*')
        liczba10 //= 3
    return ''.join(reversed(wynik))

#Zadanie 6.1.
max_napis = max(dane, key = lambda x: napis_na_liczbe10(x))
print(napis_na_liczbe10(max_napis), max_napis)

#Zadanie 6.2.
suma_liczba = sum([napis_na_liczbe10(napis) for napis in dane])
print(suma_liczba, liczba10_na_napis(suma_liczba))