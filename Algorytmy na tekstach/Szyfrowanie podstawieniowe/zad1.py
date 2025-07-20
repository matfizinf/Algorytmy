def szyfr_cezara(s, k, n):
    s_prim = []
    k_prim = k % 26
    nowy_kod = 0
    for i in range(n):
        if ord(s[i]) + k_prim > 122:
            nowy_kod = ord(s[i]) + k_prim - 26
        else:
            nowy_kod = ord(s[i]) + k_prim
        s_prim.append(chr(nowy_kod))
    return ''.join(s_prim)

s = 'interpretowanie'
wynik = szyfr_cezara(s, 107, len(s))
print(wynik)

def szyfr_beauforta(s, k, n):
    i = 0
    s_prim = []
    while i < n:
        nowy_kod = (122 - ord(s[i]) + k) % 26 + 97
        s_prim.append(chr(nowy_kod))
        i += 1
        k += i
    return ''.join(s_prim)

s = 'mapa'
wynik = szyfr_beauforta(s, 1, len(s))
print(wynik)

def szyfr_vigenerea(s, k, n, m):
    s_prim = []
    j = 0
    for i in range(n):
        k_prim = ord(k[j]) - 97
        if ord(s[i]) + k_prim > 122:
            nowy_kod = ord(s[i]) + k_prim - 26
        else:
            nowy_kod = ord(s[i]) + k_prim
        s_prim.append(chr(nowy_kod))
        j += 1
        if j >= m:
            j = 0
    return ''.join(s_prim)

s = 'jestok'
k = 'ewa'
wynik = szyfr_vigenerea(s, k, len(s), len(k))
print(wynik)