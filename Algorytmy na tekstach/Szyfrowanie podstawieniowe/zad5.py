dane = [w.strip() for w in open('slowa.txt').readlines()]
slowa_wynik = []

for s in dane:
    s_prim = []
    for z in s:
        if ord(z) + 13 > 122:
            s_prim.append(chr(ord(z) + 13 - 26))
        else:
            s_prim.append(chr(ord(z) + 13))
    s_final = ''.join(s_prim)
    if s_final[::-1] == s:
        slowa_wynik.append(s)
slowa_wynik.sort(key = lambda x: -len(x))

print(len(slowa_wynik), slowa_wynik[0])