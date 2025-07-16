def czy_anagramy2(s1, s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))

dane = [w.split()for w in open('anagram.txt').readlines()]

for w in dane:
    ile_ok = 0
    for i in range(5):
        if czy_anagramy2(w[0], w[i]):
            ile_ok += 1
    if ile_ok == 5:
        print(' '.join(w))