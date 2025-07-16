def czy_antypalindrom(n, s):
    for i in range(n // 2):
        if s[i] == s[n - i - 1]:
            return False
    return True

dane = [w.strip() for w in open('dane6.txt').readlines()]

ile = 0
for n in dane:
    if czy_antypalindrom(len(n), n):
        print(n)
        ile += 1
print(ile)