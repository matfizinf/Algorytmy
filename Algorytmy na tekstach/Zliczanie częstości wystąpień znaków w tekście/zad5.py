dane = [w.split()[0] for w in open('galerie.txt').readlines()]

#Metoda toporna

MC = {}

for k in dane:
    if k in MC:
        MC[k] += 1
    else:
        MC[k] = 1

'''for k in MC:
    print(k, MC[k])'''

#Metoda szybka
for k in set(dane):
    print(k, dane.count(k))