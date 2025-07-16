def czy_palindrom2(s):
    return ''.join(reversed(s)) == s

dane = [w.strip() for w in open('identyfikator.txt').readlines()]

for i in dane:
    s = i[:3]
    n = i[3:]
    if czy_palindrom2(s) or czy_palindrom2(n):
        print(i)