dane = [w.strip() for w in open('slowa1.txt').readlines()]

w = 'wakacje'
j = 0

for s in dane:
    ile = 0
    for z in s:
        if z == w[j]:
            j += 1
            if j == len(w):
                j = 0
                ile += 1
    if ile == 0:
        ile = len(s)
    else:
        ile = len(s) - len(w) * ile
    print(ile, end=' ')