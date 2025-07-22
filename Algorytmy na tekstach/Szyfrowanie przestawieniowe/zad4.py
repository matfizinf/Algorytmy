from math import ceil

#Sprawdzenie algorytmu
k = 3
t = 'MATURA_Z_INFORMATYKI'
szyfr = []
liczba_wierszy = k
liczba_kolumn = ceil(len(t) / k)

for i in range(liczba_wierszy):
    for j in range(liczba_kolumn):
        if j % 2 == 0:
            if i + j * liczba_wierszy < len(t):
                szyfr.append(t[i + j * liczba_wierszy])
            else:
                szyfr.append('_')
        else:
            if (j + 1) * liczba_wierszy - 1 - i < len(t):
                szyfr.append(t[(j + 1) * liczba_wierszy - 1 - i])
            else:
                szyfr.append('_')

print(''.join(szyfr))

#Zadanie 4.1. i 4.2.
k = 10
s = 'NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P'
n = len(s)
tekst = ['a'] * n
liczba_wierszy = k
liczba_kolumn = ceil(n / k)
ind = 0

for i in range(liczba_wierszy):
    for j in range(liczba_kolumn):
        if j % 2 == 0:
            tekst[i + j * liczba_wierszy] = s[ind]
        else:
            tekst[(j + 1) * liczba_wierszy - 1 - i] = s[ind]
        ind += 1

print(''.join(tekst))