dane = [w.strip() for w in open('slowa.txt')]
fragmenty = ['k{}t'.format(chr(i)) for i in range(97, 123)]

ile = 0

for s in dane:
    for f in fragmenty:
        if f in s:
            ile += 1
            break

print(ile)