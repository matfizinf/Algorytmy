from math import gcd

dane = [list(map(int, w.split())) for w in open('liczby2.txt').readlines()]
ile = 0

for w in dane:
    if gcd(w[0], w[1]) == 1:
        ile += 1

print(ile)
