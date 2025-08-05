from math import gcd
def NWD(a, b):
    if b == 0:
        return a
    else:
        return gcd(a, b)

dane = [list(map(int, w.split())) for w in open('dron.txt').readlines()]

ile = 0

for v in dane:
    nwd = NWD(abs(v[0]), abs(v[1]))
    if nwd > 1:
        ile += 1

print(ile)