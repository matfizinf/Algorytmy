from math import gcd

dane = [int(w) for w in open('liczby1.txt').readlines()]

wynik11 = open('wynik11.txt', mode='w+')

ile = 0

for liczba in dane:
    liczba_str = str(liczba)
    p = int(liczba_str[:len(liczba_str)//2])
    d = int(liczba_str[len(liczba_str)//2:])
    if gcd(p, d) == 1:
        ile += 1

wynik11.write(str(ile))
