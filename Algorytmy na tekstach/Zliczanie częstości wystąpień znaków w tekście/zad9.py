dane = open('szyfrogram.txt').read()

for a in range(65, 91):
    print(chr(a), dane.count(chr(a)))