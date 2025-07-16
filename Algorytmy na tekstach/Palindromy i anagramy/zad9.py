dane = [w.strip() for w in open('anagram2.txt').readlines()]

for l in dane:
    if len(l) == 8:
        if l.count('1') == 5 or l.count('1') == 4:
            print(l)