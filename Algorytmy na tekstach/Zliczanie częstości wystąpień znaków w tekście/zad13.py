dane = [w.strip() for w in open('slowa.txt').readlines()]

for s in dane:
    for a in range(97, 123):
        if s.count(chr(a)) * 2 >= len(s):
            print(s)
            break