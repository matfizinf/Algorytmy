dane = ''.join([c.strip() for c in open('pi.txt').readlines()])
MC = {}

for i in range(1, len(dane)):
    f = dane[i-1:i+1]
    if f in MC:
        MC[f] += 1
    else:
        MC[f] = 1

min_f = min(MC, key = lambda x: MC[x])
max_f = max(MC, key = lambda x: MC[x])

print(min_f, MC[min_f])
print(max_f, MC[max_f])