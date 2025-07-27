dane = ''.join([w.strip() for w in open('pi.txt').readlines()])

ile = 0

for i in range(len(dane) - 1):
    if int(dane[i:i+2]) > 90:
        ile += 1

print(ile)