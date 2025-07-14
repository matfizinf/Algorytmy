dane = [w.strip() for w in open('sygnaly.txt').readlines()]

#Metoda toporna

max_l_r_l1 = 0
max_s1 = ''

for s in dane:
    l_r_l = 0
    TC = [0] * 256
    for i in range(len(s)):
        if TC[ord(s[i])] == 0:
            TC[ord(s[i])] += 1
            l_r_l += 1
    if l_r_l > max_l_r_l1:
        max_l_r_l1 = l_r_l
        max_s1 = s

print(max_s1, max_l_r_l1)

#Metoda szybka

lista_posortowana = list(sorted(dane, key = lambda x: -len(set(x))))
print(lista_posortowana[0], len(set(lista_posortowana[0])))