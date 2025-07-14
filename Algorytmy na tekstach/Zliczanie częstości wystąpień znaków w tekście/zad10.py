dane = [int(w) for w in open('liczby.txt').readlines()]

TC = [0] * 10000

for l in dane:
    TC[l] += 1

print(10000 - TC.count(0))
print(TC.count(2))
print(TC.count(3))