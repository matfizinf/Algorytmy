def czy_palindrom2(s):
    return ''.join(reversed(s)) == s

dane = [w.strip() for w in open('napisy.txt').readlines()]

for n in dane:
    n1 = n + n[0]
    n2 = n[-1] + n
    if czy_palindrom2(n1):
        print(n1[len(n1) // 2], end = '')
    elif czy_palindrom2(n2):
        print(n2[len(n2) // 2], end = '')