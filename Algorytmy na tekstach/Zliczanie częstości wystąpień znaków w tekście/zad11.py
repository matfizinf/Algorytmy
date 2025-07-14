szesnastkowe = ''.join([hex(int(w))[2:].upper() for w in open('liczby2.txt').readlines()])

for c in sorted(list(set(szesnastkowe))):
    print(f'{c}: {szesnastkowe.count(c)}')