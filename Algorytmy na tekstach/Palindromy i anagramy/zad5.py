def czy_pierwsza(n):
    if n == 1:
        return False
    else:
        for d in range(2, n):
            if n % d == 0:
                return False
    return True

dane = [int(w) for w in open('pierwsze.txt').readlines()]

for l in dane:
    if czy_pierwsza(l) and czy_pierwsza(int(''.join(reversed(str(l))))):
        print(l)