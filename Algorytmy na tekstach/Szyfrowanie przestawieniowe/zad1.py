#Algorytm nr 1
def szyfrowanie_kolumnowe1(n, s, w, k):
    T = []
    t = 0
    wynik = []
    for i in range(w):
        wiersz = []
        for j in range(k):
            if t < n:
                wiersz.append(s[t])
                t += 1
            else:
                wiersz.append('X')
        T.append(wiersz)

    for i in range(k):
        for j in range(w):
            wynik.append(T[j][i])

    return ''.join(wynik)

s = 'ala ma kota i psa'
n = len(s)
w = 5
k = 4
print(szyfrowanie_kolumnowe1(n, s, w, k))

#Algorytm nr 2
def szyfrowanie_kolumnowe2(n, s, w, k):
    for i in range(n, w * k):
        s = s + 'X'

    wynik = []
    for i in range(k):
        for j in range(w):
            wynik.append(s[j * k + i])

    return ''.join(wynik)

print(szyfrowanie_kolumnowe2(n, s, w, k))