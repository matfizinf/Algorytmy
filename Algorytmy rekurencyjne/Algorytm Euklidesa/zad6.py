dane = [int(w) for w in open('liczby.txt').readlines()]

def NWD(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a

def NWD_lista(lista):
    b = lista[0]
    for a in lista:
        b = NWD(a, b)
    return b
max_nwd = 1
max_p = 0
max_k = 0

for p in range(len(dane)):
    for k in range(p, len(dane)):
        nwd = NWD_lista(dane[p:k+1])
        if nwd != 1 and k - p + 1 > max_k - max_p + 1:
            max_nwd = nwd
            max_p = p
            max_k = k

print(dane[max_p], max_k - max_p + 1, max_nwd)