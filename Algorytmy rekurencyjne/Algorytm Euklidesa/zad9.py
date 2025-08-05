from math import gcd

dane = [int(w) for w in open('skrot2.txt').readlines()]
wynik_9 = open('wynik9.txt', mode='w+')

def nieparzysty_skrot(liczba):
    return int(''.join(filter(lambda x: int(x) % 2 == 1, str(liczba))))

for liczba in dane:
    if gcd(liczba, nieparzysty_skrot(liczba)) == 7:
        wynik_9.write(f'{liczba}\n')

wynik_9.close()