#Zadanie 2.1.
d = 17

def rozmiar_tablicy(d):
    n = 1
    while n * n < d:
        n = n + 1
    return n

print(rozmiar_tablicy(d))

#Zadanie 2.2.
s = 'BTLLTU_ĘL_EOYPM_ĄPJZLCYNDREOKYLI_ZMFO_ĄGJY_Ó_N_DEWFWGISYSII_ŁEI_'
n = int(len(s) ** 0.5)

for i in range(n):
    for j in range(n):
        print(s[i + j * n], end='')
print()

#Zadanie 2.3.
tekst = 'BLĄD_JEST_PRZYWILEJEM_FILOZOFÓW_TYLKO_GŁUPCY_NIE_MYLĄ_SIĘ_NIGDY'
d = len(tekst)

n = rozmiar_tablicy(d)
s = n * n
szyfr = []

for i in range(n):
    for j in range(n):
        if i + j * n < d:
            szyfr.append(tekst[i + j * n])
        else:
            szyfr.append('_')

print(s)
print(''.join(szyfr))