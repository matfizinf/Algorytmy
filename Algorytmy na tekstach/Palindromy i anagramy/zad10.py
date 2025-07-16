def czy_palindrom2(s):
    return ''.join(reversed(s)) == s

dane = [w.strip() for w in open('symbole.txt').readlines()]

for s in dane:
    if czy_palindrom2(s):
        print(s)