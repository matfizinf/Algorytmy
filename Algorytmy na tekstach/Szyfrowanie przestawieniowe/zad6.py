from math import ceil
def szyfr_skokowy(W, k):
    wynik = ''
    n = len(W)
    m = n // k
    if n % k != 0:
        m = m + 1
    for i in range(m):
        j = i
        while j < n:
            wynik = wynik + W[j]
            j = j + m
    return wynik

W = 'SZYFROWANIE'
k = 3

print(szyfr_skokowy(W, k))

#Zadanie 6.1.
print(szyfr_skokowy('ZADANIE1JESTŁATWE', 3))
print(szyfr_skokowy('ZADANIE1JESTPROSTE', 4))

def deszyfr_skokowy(W, k):
    wynik = ['a'] * len(W)
    n = len(W)
    m = n // k

    if n % k != 0:
        m = m + 1

    ind = 0

    for i in range(m):
        j = i
        while j < n:
            wynik[j] = W[ind]
            j = j + m
            ind += 1
    return ''.join(wynik)

#Zadanie 6.2.
print(deszyfr_skokowy('UDOMEWIKAEOĆMD', 3))
print(deszyfr_skokowy('DRJTOZEBES', 4))

#Zadanie 6.3.
#Funkcja deszyfr_skokowy()

#Zadanie 6.4.
k = 3
W = 'SZYFROWANIE'

def szyfr_mieszany(W, k):
    liczba_wierszy = k
    liczba_kolumn = ceil(len(W) / k)
    pomocnicza = []
    ind = 0

    for i in range(liczba_wierszy):
        wiersz = []
        for j in range(liczba_kolumn):
            if ind < len(W):
                wiersz.append(W[ind])
            else:
                wiersz.append('_')
            ind += 1
        pomocnicza.append(wiersz)

    wynik = []

    for j in range(liczba_kolumn):
        if j % 2 == 0:
            for i in range(liczba_wierszy):
                if pomocnicza[i][j] != '_':
                    wynik.append(pomocnicza[i][j])
        else:
            for i in range(liczba_wierszy - 1, -1, -1):
                if pomocnicza[i][j] != '_':
                    wynik.append(pomocnicza[i][j])

    return ''.join(wynik)