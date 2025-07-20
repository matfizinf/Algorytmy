#Zadanie 7.1.
def kod(x):
    return ord(x)

def znak(y):
    return chr(y)

def szyfruj(zn, k):
    k_prim = k % 26
    if kod(zn) + k_prim > 90:
        return znak(kod(zn) + k_prim - 26)
    else:
        return znak(kod(zn) + k_prim)

def deszyfruj(zn, k):
    k_prim = k % 26
    if kod(zn) - k_prim < 65:
        return znak(kod(zn) - k_prim + 26)
    else:
        return znak(kod(zn) - k_prim)

#Zadanie 7.2.
s1 = 'INFORMATYKA'
s1_prim = []

for i, z in enumerate(s1):
    s1_prim.append(szyfruj(z, i + 1))
print(''.join(s1_prim))

s2 = 'LQPTZZLZ'
s2_prim = []

for i, z in enumerate(s2):
    s2_prim.append(deszyfruj(z, i + 1))
print(''.join(s2_prim))

#Zadanie 7.3.
def deszyfruj_slowo(n, S):
    S_prim = []
    for i, z in enumerate(S):
        S_prim.append(deszyfruj(z, i + 1))
    return ''.join(S_prim)