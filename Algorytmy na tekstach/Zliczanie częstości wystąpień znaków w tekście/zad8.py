dane = [w.strip() for w in open('dane6.txt').readlines()]

TC = [0] * 11

for p in range(2, 11):
    for s in dane:
        if int(max(s)) == p - 1:
            TC[p] += 1

for p in range(2, 11):
    print(p, TC[p])